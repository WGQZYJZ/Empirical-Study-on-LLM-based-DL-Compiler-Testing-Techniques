
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
other = torch.randn(1, 1) * 0.8678984851060165
x1 = torch.randn(1, 2, 64, 64)
