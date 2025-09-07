
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1, x2):
        v1  = self.linear(x1)
        v2  = x2 + v1
        return relu(v2)


# Inputs to the model
x1  = torch.randn(1, 64)
x2  = torch.randn(1, 32)
__output__  = m(x1, x2)


