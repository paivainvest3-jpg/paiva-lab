# Document Intake Agent

**Status:** lab demonstrativo criado para portfólio  
**Categoria:** RAG / Document AI / Reliable Agents

## Cenário
Triagem manual de documentos recebidos por uma operação: identificar tipo, extrair campos, validar consistência e decidir para qual fila encaminhar.

## Arquitetura
1. ingestão e hash do arquivo;
2. extração de texto/metadados;
3. classificação com schema fechado;
4. extração estruturada;
5. validações determinísticas;
6. confidence threshold;
7. abstention quando faltam evidências;
8. human-in-the-loop para exceções;
9. trilha de auditoria e eval dataset.

## Exemplo de output
```json
{
  "document_type": "proof_of_address",
  "confidence": 0.94,
  "fields": {
    "name": "EXAMPLE PERSON",
    "issue_date": "2026-08-01"
  },
  "validation": {
    "required_fields_present": true,
    "date_within_policy": true
  },
  "route": "auto_approved"
}
```

## O que demonstra
O diferencial não é “usar LLM em PDF”; é desenhar um sistema que sabe quando automatizar, quando se abster e como provar o que fez.
