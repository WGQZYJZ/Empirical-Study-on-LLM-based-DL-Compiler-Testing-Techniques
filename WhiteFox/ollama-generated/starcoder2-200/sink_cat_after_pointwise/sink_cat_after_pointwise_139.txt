
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v  = torch.cat([x1, x2], dim=0) # Concatenate tensors along the first dimension (dimension of batch size).
        return torch.relu(v), v

m = Model()

x1 = torch.randn(3,4) # A random tensor to concatenate with other tensors in the model.
__output__, y  = m(torch.ones([2,4]), x1)

