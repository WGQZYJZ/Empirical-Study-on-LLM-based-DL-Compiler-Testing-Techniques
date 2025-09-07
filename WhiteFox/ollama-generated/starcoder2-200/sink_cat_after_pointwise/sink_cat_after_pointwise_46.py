
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, self._x2], dim=0)  # Concatenate tensors along a dimension
        v2 = v1.view(-1, 16384)  # Reshape the concatenated tensor to a 2D matrix
        v3 = torch.relu(v2)  # Apply ReLU operation
        return v3

# Initializing the model with two input tensors