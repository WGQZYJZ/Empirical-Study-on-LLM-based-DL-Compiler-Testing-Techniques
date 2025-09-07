
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 4 * 4, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32 * 4 * 4))
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
other = torch.randn(64)
x1 = torch.randn(64, 32, 4, 4)
