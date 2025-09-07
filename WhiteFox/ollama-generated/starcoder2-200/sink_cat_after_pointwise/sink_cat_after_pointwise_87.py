

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Concatenate 2 tensors along axis 0 and then reshape it to 4D shape after squeezing
        v1 = torch.cat([x1, x1], dim=0).squeeze()
        # Reshape the concatenated tensor from 3D (5, 6) -> 4D (?, ?, ? 5) 
        v2 = v1.view(-1, 3, 8)
        # Apply a pointwise operation on the reshaped tensor.
        v3 = torch.relu(v2)

        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 6)

