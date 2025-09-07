
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.norm = torch.nn.LayerNorm(512)
        self.attn = torch.nn.MultiheadAttention(
            512, 8, dropout=0.1)
        self.mlp = torch.nn.Sequential(
            torch.nn.Linear(512, 4 * 512),
            torch.nn.ReLU(),
            torch.nn.Linear(4 * 512, 512))
 
    def forward(self, q):
        v1  = self.norm(q)
        v2, _  = self.attn(v1, v1)
        v3  = self.mlp(v1 + v2) 
        return v3

# Initializing the model
m  = MyModel()

# Inputs to the model
q  = torch.randn(64, 512)
__output__  = m(q)

