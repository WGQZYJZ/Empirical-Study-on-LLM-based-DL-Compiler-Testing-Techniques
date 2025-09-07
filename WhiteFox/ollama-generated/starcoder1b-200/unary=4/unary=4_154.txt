
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 30)
 
    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=1)
        v2 = torch.matmul(v1, 0.5).reshape(1, -1)
        v3 = torch.matmul(v1, 0.7071067811865476).reshape(1, -1)
        v4 = torch.erf(v3) + 1
        v5 = torch.matmul(v2, v4).reshape(1, -1)
        v6 = v5 * torch.sqrt(torch.exp(-torch.pow(v5, 2)))
        return v6


# Initializing the model
m = Model()

