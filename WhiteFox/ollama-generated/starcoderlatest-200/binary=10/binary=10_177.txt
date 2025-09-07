
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.reshape(-1)) + other
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 256)
