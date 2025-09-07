
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.nn.Parameter(torch.randn((3, 4)))
 
    def forward(self, x1):
        v1  = torch.mm(x1, x2) # Apply pointwise convolution with kernel size 1 to the input tensor
        return v1

m = Model()


