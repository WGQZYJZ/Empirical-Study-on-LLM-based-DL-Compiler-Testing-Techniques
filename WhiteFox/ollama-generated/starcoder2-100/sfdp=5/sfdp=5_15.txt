
class Model(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, dim_feedforward=2048, dropout=0.1, activation="relu"):
        super().__init__()
 
        self.encoder = torch.nn.TransformerEncoderLayer(d_model, nhead)
 
    def forward(self, src):
        src = self.encoder(src) 
        return src

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(40960753, 528).reshape(-1, 76, 70).transpose(1, 2)
__output__= m(x1)
