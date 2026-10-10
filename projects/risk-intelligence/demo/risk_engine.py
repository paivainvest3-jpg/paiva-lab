"""Synthetic risk-intelligence demo.
No production data or proprietary rules are used.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

SEED = 42
rng = np.random.default_rng(SEED)
N = 6000


def make_data(n: int = N) -> pd.DataFrame:
    df = pd.DataFrame({
        "account_age_days": rng.gamma(3.0, 55.0, n).clip(0, 900),
        "event_velocity_1h": rng.poisson(3.0, n),
        "linked_entities": rng.poisson(1.2, n),
        "device_reuse": rng.beta(1.4, 7.0, n),
        "behavior_similarity": rng.beta(2.0, 4.0, n),
        "amount_zscore": rng.normal(0, 1.0, n),
        "failed_attempts_24h": rng.poisson(0.7, n),
        "cashout_ratio": rng.beta(2.0, 3.0, n),
    })

    latent = (
        -0.010 * df.account_age_days
        + 0.22 * df.event_velocity_1h
        + 0.38 * df.linked_entities
        + 2.4 * df.device_reuse
        + 2.1 * df.behavior_similarity
        + 0.35 * df.failed_attempts_24h
        + 1.0 * df.cashout_ratio
        + 0.25 * np.abs(df.amount_zscore)
        - 3.2
    )
    prob = 1 / (1 + np.exp(-latent))
    df["label"] = rng.binomial(1, prob)
    return df


def main() -> None:
    df = make_data()
    features = [c for c in df.columns if c != "label"]
    X = df[features]
    y = df["label"]

    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    clusterer = KMeans(n_clusters=5, random_state=SEED, n_init="auto")
    df["cluster"] = clusterer.fit_predict(Xs)

    X_model = df[features + ["cluster"]]
    Xtr, Xte, ytr, yte = train_test_split(
        X_model, y, test_size=0.25, random_state=SEED, stratify=y
    )
    model = HistGradientBoostingClassifier(max_depth=4, learning_rate=0.08, random_state=SEED)
    model.fit(Xtr, ytr)
    proba = model.predict_proba(Xte)[:, 1]
    pred = (proba >= 0.50).astype(int)

    print("Synthetic Risk Intelligence Engine")
    print("=" * 36)
    print(f"Rows: {len(df):,} | Positive rate: {y.mean():.2%}")
    print(f"ROC AUC: {roc_auc_score(yte, proba):.3f}")
    print(classification_report(yte, pred, digits=3))

    scored = Xte.copy()
    scored["risk_score"] = (proba * 100).round(1)
    scored["label"] = yte.to_numpy()
    print("\nTop scored examples:")
    print(scored.sort_values("risk_score", ascending=False).head(10).to_string(index=False))

    print("\nCluster summary:")
    summary = df.groupby("cluster").agg(
        users=("label", "size"),
        positive_rate=("label", "mean"),
        avg_velocity=("event_velocity_1h", "mean"),
        avg_linked=("linked_entities", "mean"),
        avg_similarity=("behavior_similarity", "mean"),
    )
    print(summary.round(3).to_string())


if __name__ == "__main__":
    main()
