
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 10, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = v1 + x2
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(50, 32 * 10)
