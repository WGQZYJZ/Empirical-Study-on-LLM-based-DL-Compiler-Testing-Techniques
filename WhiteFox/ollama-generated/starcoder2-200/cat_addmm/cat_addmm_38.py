
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()

    def forward(self, x1, m1, m2):
        v1  = torch.addmm(x1, m1, m2)
        v2  = torch.cat([v1],dim)
        return v2


# Initializing the model
m  = Model() # The shape of input tensors x1 is (100, 5), and mat1 has shape [3,4]. dim parameter for torch.nn.Cat, whose default value is 1.

# Inputs to the model
x1  = torch.randn(100, 5)
m1  = torch.randn(3, 4)
m2  = torch.randn(4, 6)

