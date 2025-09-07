

class Model(torch.nn.Module):
    def __init__(self, size1, size2):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1] * 3) # Concatenate the input three times along dimension -1 (in the current implementation, it is dim=-1).
        v2 = v1.view(-1, 10) # Reshape this concatenated tensor to a 1-dimensional vector of length 30.
        v3 = torch.relu(v2) # Apply ReLU unary operation on this reshaped input vector.
        return v3


# Initializing the model
m = Model(size1, size2)

# Inputs to the model
x1  = torch.randn(50)
