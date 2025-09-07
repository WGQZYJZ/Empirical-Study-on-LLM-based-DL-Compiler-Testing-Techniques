
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.layer_1 = torch.nn.Linear(hidden_size, hidden_size)
        self.layer_2 = torch.nn.Linear(hidden_size, 1)
 
    def forward(self, x1):
        v1 = self.layer_1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model(hidden_size=8)


# Inputs to the model
x1 = torch.randn(1, 8, 128, 128)
