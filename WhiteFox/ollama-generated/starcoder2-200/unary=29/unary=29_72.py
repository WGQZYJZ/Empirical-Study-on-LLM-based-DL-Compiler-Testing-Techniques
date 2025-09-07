
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 5)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.clamp_min(v1, min=0.) # Clamp the output of the transposed convolution to a minimum value, here we use zero.
        v3  = torch.clamp_max(v2, max=1.) # Clamp the output of the previous operation to a maximum value, here we use one.
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(10, 3, 64, 64)

__output__  = m(x1)
