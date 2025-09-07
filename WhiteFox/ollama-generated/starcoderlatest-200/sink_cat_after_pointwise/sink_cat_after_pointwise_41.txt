
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=...)
        v2 = v1.view(...)
        v3 = torch.relu(v2)
        return v3
# Inputs to the model
x1 = torch.randn(4, 2, 2)
x2 = torch.randn(16, 2, 2)
