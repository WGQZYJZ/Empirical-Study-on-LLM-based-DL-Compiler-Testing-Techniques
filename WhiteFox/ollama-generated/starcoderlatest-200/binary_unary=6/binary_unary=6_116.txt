
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = F.relu(v2)
        return v3
# Inputs to the model
other = torch.randn(1024)
x1 = torch.randn(1, 1024, 64, 64)
