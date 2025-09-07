
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension (0 is the first dimension)
        v2 = v1.view(-1)  # Reshape the concatenated tensor (-1 is the second dimension)
        v3 = self.relu(v2)  # Apply a pointwise unary operation to the reshaped tensor
        return v3
