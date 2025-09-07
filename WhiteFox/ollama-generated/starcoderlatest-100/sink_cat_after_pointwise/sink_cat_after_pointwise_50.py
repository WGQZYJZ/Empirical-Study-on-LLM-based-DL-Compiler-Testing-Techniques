
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate input tensors along the dimension 1 (columns)
        t3 = v1.view(...)  # Reshape the concatenated tensor
        return torch.relu(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
