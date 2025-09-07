
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0) # Concatenate tensors along a dimension
        v2  = v1.view(-1, 48)            # Reshape the concatenated tensor
        v3  = torch.relu(v2)              # Apply ReLU to the reshaped tensor.
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 72)
x2 = torch.randn(60, 8*5 * 9)
__output__  = m(x1, x2).detach().numpy()

