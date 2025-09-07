
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0) # Concatenate tensors along a dimension
        v2  = v1.view(-1, 36)             # Reshape the concatenated tensor
        v3  = F.relu(v2)                  # Apply a pointwise unary operation to the reshaped tensor
        return v3


# Initializing the model