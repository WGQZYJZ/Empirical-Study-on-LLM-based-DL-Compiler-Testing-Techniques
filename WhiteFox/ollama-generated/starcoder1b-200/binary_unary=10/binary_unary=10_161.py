
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 5
        v2 = relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 8)
