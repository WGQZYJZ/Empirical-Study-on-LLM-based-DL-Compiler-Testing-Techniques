
class Model(torch.nn.Module):
    def __init__(self, ndim):
        super().__init__()
        self.ndim = ndim
        if ndim > 1:
            self.conv = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
            self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        out = torch.nn.functional.convXd(...)(x) 
        if self.ndim > 1:
            bn_in = out 
            bn_out = bn(bn_in)
            return bn_out
        else:
            return out

# Initializing the model
m = Model(2)

 # Inputs to the model
x = torch.randn(1, 16, 48, 10, 56)
