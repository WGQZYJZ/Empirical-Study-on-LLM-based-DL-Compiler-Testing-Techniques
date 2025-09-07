
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, 2*x1], dim=1) # Concatenate tensors along a dimension of the tensor (dim=-1 in PyTorch API)
        t2 = t1.view(t1.shape[0]*t1.shape[2], -1) # Reshape the concatenated tensor
        t3 = torch.relu(t2) # Apply a pointwise unary operation to the reshaped tensor
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5, 6)
