
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(128, 3)
        self.key  = torch.nn.Linear(256, 3)
 
    def forward(self, x):
        v1  = self.query(x) 
        v2  = self.key(v1).transpose(-2, -1) # [B*D]
        return v2

# Initializing the model
m  = TransformerModel()
 
# Inputs to the model
x_i = torch.randn(300, 512, 32)   # input
__output__  = m(x_i)

