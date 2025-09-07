
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 1
        v2 = relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
