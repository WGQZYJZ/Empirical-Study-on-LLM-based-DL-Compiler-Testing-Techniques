
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim):
        super().__init__()
        self.query = torch.nn.Linear(query_dim, 8)
        self.key = torch.nn.Linear(key_dim, 8)
 
    def forward(self, x1):
        v1 = torch.matmul(self.query(x1), self.key(x1).transpose(-2, -1))
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model(query_dim=1, key_dim=1)

# Inputs to the model
x1 = torch.randn(1, 1, 8)
