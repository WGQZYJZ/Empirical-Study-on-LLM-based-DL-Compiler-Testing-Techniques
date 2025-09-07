
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 3)
 
    def forward(self, x1, x2=None):
        v1 = self.linear(x1) + x2
        return relu(v1)


# Inputs to the model
x1 = torch.randn(1, 32)
x2 = torch.randn(1, 8)
