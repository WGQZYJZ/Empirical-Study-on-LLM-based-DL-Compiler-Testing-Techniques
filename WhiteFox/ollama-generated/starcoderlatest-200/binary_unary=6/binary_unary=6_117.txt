
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = v1 - 0.5
        v3 = torch.relu(v2)
        return v3

# Inputs to the model
x2 = torch.randn(4, 32)
