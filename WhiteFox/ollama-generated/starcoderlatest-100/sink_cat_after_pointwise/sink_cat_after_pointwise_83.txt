
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=2)  # Concatenate two tensors along the third dimension.
        v2 = v1.view(-1)  # Reshape the concatenated tensor into a single vector.
        v3 = torch.nn.functional.relu(v2)  # Apply ReLU on the reshaped vector.
        return v3

# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
