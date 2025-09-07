
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16 * 28, 4096)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1))
        v2 = v1 - 3
        v3 = torch.relu(v2)
        return v3

# Inputs to the model
x1 = torch.randn(1, 16 * 28)
