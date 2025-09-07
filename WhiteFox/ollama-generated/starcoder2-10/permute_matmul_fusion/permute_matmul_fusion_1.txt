
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.permute(x1, 0, -1) # Permute the input tensor A (with more than 2 dimensions).
        v2 = torch.bmm(v1, x2)
        return v2

m = Model()
x1  = torch.randn(3,4) # Generate input tensor_A with more than 2 dimensions.
x2  = torch.randn(3,4) # Generate input tensor_B with more than 2 dimensions.
__output__  = m(x1, x2)

