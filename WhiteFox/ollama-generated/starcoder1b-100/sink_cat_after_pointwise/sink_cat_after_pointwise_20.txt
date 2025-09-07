
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate tensors along a dimension
        v2 = v1.view(-1, 4)        # Reshape the concatenated tensor
        return torch.relu(v2)


# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 4)
