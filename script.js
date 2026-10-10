const fields = ['accounts','velocity','similarity','newness'];
const weights = {accounts:2.8, velocity:.30, similarity:.28, newness:.18};

function updateScore(){
  const v = Object.fromEntries(fields.map(id=>[id,Number(document.getElementById(id).value)]));
  fields.forEach(id=>document.getElementById(id+'Out').textContent=v[id]);

  const raw = (v.accounts-1)*weights.accounts
    + v.velocity*weights.velocity
    + v.similarity*weights.similarity
    + v.newness*weights.newness;

  const score = Math.max(0,Math.min(100,Math.round(raw)));
  document.getElementById('score').textContent=score;

  const ring=document.getElementById('scoreRing');
  ring.style.background=`conic-gradient(var(--cyan) ${score*3.6}deg,#152534 0deg)`;

  let label='Baixo',
      text='Comportamento dentro da faixa esperada.',
      cls='#79e7aa',
      bg='#153027';

  if(score>=70){
    label='Alto';
    text='Priorizar revisão: combinação forte de sinais de coordenação e velocidade.';
    cls='#ff7b7b';
    bg='#331c22';
  } else if(score>=40){
    label='Médio';
    text='Solicitar evidências adicionais ou aplicar monitoramento reforçado.';
    cls='#ffca68';
    bg='#362d17';
  }

  const el=document.getElementById('riskLabel');
  el.textContent=label;
  el.style.color=cls;
  el.style.background=bg;

  document.getElementById('riskText').textContent=text;

  const parts=[
    ['Contas relacionadas',Math.min(100,(v.accounts-1)*10)],
    ['Velocidade',v.velocity],
    ['Similaridade',v.similarity],
    ['Novidade',v.newness]
  ];

  document.getElementById('signalBars').innerHTML=parts
    .map(([n,x])=>`<div><small>${n} · ${Math.round(x)}</small><div class="bar"><i style="width:${x}%"></i></div></div>`)
    .join('');
}

fields.forEach(id=>document.getElementById(id).addEventListener('input',updateScore));
updateScore();
