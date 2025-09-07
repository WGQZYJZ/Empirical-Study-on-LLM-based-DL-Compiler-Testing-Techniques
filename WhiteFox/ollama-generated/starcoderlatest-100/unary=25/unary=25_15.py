
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * -0.35
        v4 = torch.where(v1, v2, v1)
        return v4


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
