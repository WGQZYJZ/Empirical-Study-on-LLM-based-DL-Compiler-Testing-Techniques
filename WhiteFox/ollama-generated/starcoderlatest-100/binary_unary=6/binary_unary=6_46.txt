
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1280, 512)
 
    def forward(self, x1, other=torch.ones_like(x1)):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = F.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(16, 1280)
other = x1
