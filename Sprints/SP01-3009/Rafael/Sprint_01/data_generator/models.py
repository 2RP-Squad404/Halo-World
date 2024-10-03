from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class FictionalPerson(BaseModel):
    id_pessoa: str
    nome: str
    cpf: str
    data_nascimento: datetime
    sexo: Optional[str]
    estado_civil: Optional[str]
    nacionalidade: Optional[str]
    endereco: Optional[str]
    telefone: Optional[str]
    email: Optional[str]
    data_criacao_registro: datetime


class FictionalAccount(BaseModel):
    id_conta: str
    num_conta: str
    tipo_conta: str
    status_conta: str
    data_abertura: datetime
    data_encerramento: Optional[datetime]
    saldo_conta: float
    id_cliente: str
    data_ultima_movimentacao: Optional[datetime]


class FictionalCard(BaseModel):
    id_cartao: str
    id_produto_cartao: Optional[str] = None
    num_cartao: str
    num_seq_via_cartao: str
    id_conta: str
    num_cpf_cliente: str
    cod_tip_portador: str
    num_bin: str
    cod_loja_emis_cartao: Optional[str] = None
    id_cliente_so: str
    dth_emis_cartao: datetime
    dth_embs_cartao: Optional[datetime] = None
    dth_valid_cartao: datetime
    dth_desbloqueio: Optional[datetime] = None
    cod_sit_cartao: str
    des_sit_cartao: str
    dth_sit_cartao: datetime
    cod_estagio_cartao: str
    des_estagio_cartao: str
    dth_estagio_cartao: datetime
    flg_embs_loja: str
    flg_cartao_cancelado: str
    flg_cartao_provisorio: str
    flg_conta_cancelada: Optional[str] = None
    dth_ult_atu_so: datetime
    num_seq_ult_alteracao: str
    dth_inclusao_reg: datetime
    pt_nomeplastico: str
    ca_arquivolote: Optional[str] = None
    ca_id_imagem: Optional[str] = None
    bc_responsavel: Optional[str] = None
    ca_codigocancelamento: Optional[str] = None
    ca_flaggeracartasenha: Optional[str] = None
    pt_id_imagem: Optional[str] = None
