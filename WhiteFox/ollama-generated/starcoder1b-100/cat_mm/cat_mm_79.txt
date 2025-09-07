
class Model(torch.nn.Module):
    def __init__(self, dim: int = 2):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2 = [v1] + [v1]*(self.dim - 1)
        return torch.cat(v2, dim=self.dim-1)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(4, 3, 512, 512)
