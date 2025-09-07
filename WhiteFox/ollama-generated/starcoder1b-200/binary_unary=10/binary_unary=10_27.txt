
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + torch.randn(16)
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x = torch.randn(8, 32)
