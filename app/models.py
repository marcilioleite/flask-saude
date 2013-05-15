from app import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id              = db.Column(db.Integer, primary_key=True)
    nome            = db.Column(db.String(255))
    data_nascimento = db.Column(db.Date)
    sexo            = db.Column(db.String(1))
    responsavel_id  = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    responsavel     = db.Relationship('Paciente', backref='responsavel')
    email           = db.Column(db.String(255), unique=True)
    certidao        = db.Column(db.String(50), unique=True)
    rg              = db.Column(db.String(50), unique=True)
    cpf             = db.Column(db.String(50), unique=True)
    telefone        = db.Column(db.String(50))
    celular         = db.Column(db.String(50))
    cep             = db.Column(db.String(50))
    endereco        = db.Column(db.String(255))
    numero          = db.Column(db.String(50))
    complemento     = db.Column(db.String(255))
    bairro          = db.Column(db.String(255))
    cidade          = db.Column(db.String(255))
    estado          = db.Column(db.String(2))
    sus             = db.Column(db.String(50))
    tipo_sanguineo  = db.Column(db.String(2))
    agendamentos    = db.Relationship('Consulta', backref='paciente')
    consultas       = db.Relationship('Consulta', backref='paciente')

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    
    id          = db.Column('id', db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    telefone    = db.Column(db.String(50))
    celular     = db.Column(db.String(50))
    sus         = db.Column(db.String(50))
    data        = db.Column(db.Date)
    inicio      = db.Column(db.Time)
    fim         = db.Column(db.Time)

class Consulta(db.Model):
    __tablename__ = 'consultas'
    
    id          = db.Column('id', db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    data        = db.Column(db.Date)
    inicio      = db.Column(db.Time)
    fim         = db.Column(db.Time)
    
    queixa   = db.Column(db.String(255))
    historia = db.Column(db.Text)
    
    altura             = db.Column(db.Float)
    peso               = db.Column(db.Float)
    batimentos         = db.Column(db.Integer)
    pressao_sistolica  = db.Column(db.Integer)
    pressao_diastolica = db.Column(db.Integer)
    
    observacoes = db.Column(db.Text)
    diagnostico = db.Column(db.Text)
    
    evolucao   = db.Column(db.Text)
    prescricao = db.Column(db.Text)
    
