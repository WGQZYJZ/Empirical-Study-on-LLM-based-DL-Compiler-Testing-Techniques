class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        v1  = torch.cat([t1, t2], dim=0) # Concatenate tensors along the first dimension (axis 0).
        v2  = v1.view(-1, v1.size()[-2] * v1.size()[-1]) # Reshape the concatenated tensor.
        v3  = torch.nn.functional.relu(v2) # Apply a pointwise unary operation to the reshaped tensor.
        return v3


# Initializing the model
m  = Model()
__input_t1__, __input_t2__  = torch.randn(4, 5), torch.randn(9, 8)

# Output of the model for the given inputs t1 and t2.
