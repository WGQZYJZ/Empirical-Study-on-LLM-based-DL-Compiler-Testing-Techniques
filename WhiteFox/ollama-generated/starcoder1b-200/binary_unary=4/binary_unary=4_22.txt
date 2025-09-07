
class Model(torch.nn.Module):
    def __init__(self, other=10):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x2, other=10):
        v2 = self.linear(x2) + other
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x2 = torch.randn(1, 4, requires_grad=True)
