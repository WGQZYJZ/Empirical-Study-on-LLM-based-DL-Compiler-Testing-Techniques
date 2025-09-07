
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        v = torch.cat([t1, t2], dim=-1) # Concatenate two tensors
        vv = v.view(-1, 4)   # Reshape the concatenated tensor with shape (4, 2).
        vv = torch.relu(vv)   # Apply a pointwise unary operation to the reshaped tensor with shape (4, 2).
        return vv


# Initializing the model
m = Model()
t1 = torch.randn(2, 3)
t2 = torch.randn(2, 3)

