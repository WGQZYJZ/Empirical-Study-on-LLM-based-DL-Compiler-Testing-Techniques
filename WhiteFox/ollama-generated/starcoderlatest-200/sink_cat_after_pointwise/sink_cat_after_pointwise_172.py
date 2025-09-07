
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=-1) # Concatenate three tensors along -1 dimension
        v2 = v1.view(-1, 9)
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(4, 5, 7)
x2 = torch.randn(8, 10, 21)
x3 = torch.randn(6, 2, 21)
