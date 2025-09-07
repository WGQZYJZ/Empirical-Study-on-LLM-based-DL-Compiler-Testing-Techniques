
class TransformerLayer(torch.nn.Module):
    def __init__(self, hidden_dim, nhead=8):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(hidden_dim, nhead)
        self.norm1 = torch.nn.BatchNorm2d(hidden_dim)
        self.ff    = torch.nn.Linear(4*hidden_dim, hidden_dim)
        self.norm2 = torch.nn.BatchNorm2d(hidden_dim)
 
    def forward(self, x1):
        x1 = self.attn(x1)[0]
        v1 = x1 + x1
        v2 = self.norm1(v1)
        y1 = self.ff(torch.cat((v2, v1), dim=1))
        v3 = self.norm2(y1)
        return v3
 

class TransformerEncoder(torch.nn.Module):
    def __init__(self, num_layers, hidden_dim, nhead=8):
        super().__init__()
        self.model = torch.nn.Sequential()
        for _ in range(num_layers):
            self.model.add_module('layer_%d'%_, TransformerLayer(hidden_dim, nhead))
 
    def forward(self, x1):
        return self.model(x1)
 

class Model(torch.nn.Module):
    def __init__(self, num_layers=4):
        super().__init__()
        self.enc = TransformerEncoder(num_layers, 64)
 
    def forward(self, x1):
        x1 = self.enc(x1)
        return x1
 

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(128, 3, 64, 64)
