
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v = self.linear(x)
        return -v


# Inputs to the model
inputs = torch.randn(50, 32)
