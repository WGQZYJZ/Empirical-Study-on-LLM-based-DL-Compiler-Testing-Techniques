
class TransformerModel(torch.nn.Module):
    def __init__(self, ninp, nhead, nhid, nlayers, dropout=0.5):
        super().__init__()
        self.model = torch.nn.TransformerEncoderLayer(d_model  =ninp, dim_feedforward = nhid, nhead = nhead)
        self.droput = torch.nn.Dropout(p=dropout)
 
    def forward(self, src, tgt):
        return self.model(src), self.droput(tgt)

 # Initializing the model
 m  = TransformerModel(ninp = 768, nhead = 12, nhid = 3072, nlayers=12, dropout = 0.5)
 
# Inputs to the model
src  = torch.rand(3, 45, 768)
tgt  = torch.rand(3, 45, 3072)

 # Model 1
 m_1  = TransformerModel(ninp=768, nhead=12, nhid=3072, nlayers=12, dropout=0.5)(src, tgt)
 
 # Model 2 
 m_2  = TransformerModel(ninp=768, nhead=12, nhid=3072, nlayers=12, dropout=0.5)(tgt, src)


# Initializing the model
 m  = TransformerModel(ninp = 64, nhead = 8, nhid = 256, nlayers=6, dropout = 0.3)
 
# Inputs to the model
src  = torch.rand(197, 32, 64)

 # Model 1 
 m_1  = TransformerModel(ninp=64, nhead=8, nhid=256, nlayers=6, dropout=0.3)(src)
 
# Model 2 
m_2  = TransformerModel(ninp=64, nhead=8, nhid=256, nlayers=6, dropout=0.3)(torch.rand(197, 32, 64))

 # Initializing the model
 m  = TransformerModel(ninp = 768, nhead = 12, nhid = 3072, nlayers=12, dropout = 0.5)
 
# Inputs to the model
src  = torch.rand(3, 45, 768)

 # Model 1 
 m_1  = TransformerModel(ninp=768, nhead=12, nhid=3072, nlayers=12, dropout=0.5)(src)
 
