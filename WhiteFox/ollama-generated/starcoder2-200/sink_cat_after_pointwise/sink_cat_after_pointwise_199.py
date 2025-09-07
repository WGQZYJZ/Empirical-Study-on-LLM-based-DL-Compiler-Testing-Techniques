
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension.
        v2 = v1.view(-1, 3 * 48)  # Reshape the concatenated tensor.
        return torch.nn.functional.tanh(v2).permute((0, 2, 1))

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3,48)
x2 = torch.randn(3, 48)
__output__  = m(x1, x2).permute((0,2,1))