
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        v2 = relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 4)
