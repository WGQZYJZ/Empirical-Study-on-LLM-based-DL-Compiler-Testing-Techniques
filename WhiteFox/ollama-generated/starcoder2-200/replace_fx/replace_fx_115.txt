
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1) # Generates a tensor with the same size as input filled with random numbers 
        return x1 + v2

m = Model()

x1 = torch.randn(5000, 64, 703) # A random input
