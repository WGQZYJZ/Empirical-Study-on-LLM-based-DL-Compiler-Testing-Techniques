
class Model(torch.nn.Module):
    def __init__(self, dim=1000):
        super().__init__()
        self.dense = torch.nn.Linear(dim, 64)
        self.norm = torch.nn.LayerNorm(8)
 
    def forward(self, x1):
        v1 = self.norm(self.dense(x1))
        v2 = torch.softmax(v1, dim=-1).transpose(-2, -1)
        return v2


# Initializing the model
m  = Model()
v1 = torch.randn(100, 8, 64)
