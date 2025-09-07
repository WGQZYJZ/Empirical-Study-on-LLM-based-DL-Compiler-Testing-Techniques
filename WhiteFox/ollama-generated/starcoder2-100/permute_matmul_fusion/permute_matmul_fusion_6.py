
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # Both tensors have shape (batch_size, 3072)
        v1 = x1.permute([0, 2, 1])
        v2 = x2.permute([0, 2, 1])
        return torch.bmm(v1, v2).sum()


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 3072) # Shape of a PyTorch tensor is (batch_size, dim_1, dim_2...)
x2 = torch.randn(5, 3072) # Shape of a PyTorch tensor is (batch_size, dim_1, dim_2...)


# Input shape after permuting the tensors to be compatible with the bmm operation in the forward method above: x1 is (5, 3, 3072), and x2 is (5, 3072, 3)


