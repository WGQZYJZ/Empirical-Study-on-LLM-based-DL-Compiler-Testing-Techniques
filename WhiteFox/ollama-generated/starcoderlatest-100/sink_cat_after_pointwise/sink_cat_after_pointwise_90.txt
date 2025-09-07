
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along axis 0 (the dimension of batch size)
        t2 = t1.view(2, -1)  # Reshape the concatenated tensor
        t3 = torch.relu(t2)  # Apply a pointwise unary operation to the reshaped tensor
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 2, 10)
x2 = torch.randn(6, 4, 10)
