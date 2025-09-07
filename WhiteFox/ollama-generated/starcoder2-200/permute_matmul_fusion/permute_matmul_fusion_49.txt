
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2) # Input A
        v3 = torch.permute(v1, (0, 1)) # Permute the input tensor of shape [1] to shape [1, 2]

        v5 = torch.bmm(
            torch.permute(x1.reshape(4), 1).reshape(-1, x1.shape[0]),
            torch.permute(v3.reshape(1, -1).expand_as(x1.reshape(4, x1.shape[2], x1.shape[3])), (-1, 2)))
        return v5

# Initializing the model
m = Model()

 # Inputs to the model A
x1 = torch.randn(2)
__outputA__ = m(x1)

# Inputs to the model B
v4 = torch.bmm(
    torch.permute(torch.randn(4).reshape(-1, x1.shape[0]), 1), 
    torch.permute(x1.reshape(-1, x1.shape[2], x1.shape[3]).reshape(1, -1)))
__outputB__ = m(v4)

