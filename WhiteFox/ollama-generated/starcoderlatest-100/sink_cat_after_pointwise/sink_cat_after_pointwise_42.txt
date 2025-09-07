
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x2, ...], dim=3)
        v2 = v1.view(-1, 4) # Reshape to a vector for linear transformation
        v3 = torch.relu(v2)
        return v3

# Inputs to the model
x1 = torch.randn(1, 50, 8, 8)
x2 = torch.randn(1, 50, 8, 4)
