
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x1):
        v1   = self.conv(x1)
        vout = v1 - self.other # subtracting another tensor or scalar from the output of convolution
        return vout

# Initializing the model with a 4-by-3-sized tensor as 'other' parameter to be substracted from the output of the conv layer.
m = Model(torch.zeros((1, 8, 64, 64)))

 # Inputs to the model: we need two tensors for this case. One is the input to the convolution and another tensor that will be subtracted from it. 
x1, other = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 64, 64)
