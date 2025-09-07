
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1 = self.conv(x1)
         return torch.tanh(v1 + other),  # A new tensor is returned (added to the output of the convolution).
# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn_like(x1) # This is the new tensor added as a keyword argument of addition operation in forward function

__output__, __output2__ = m(x1)

