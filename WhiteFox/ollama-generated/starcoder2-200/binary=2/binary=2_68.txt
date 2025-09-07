
class Model(torch.nn.Module):
    def __init__(self, conv):
        super().__init__()
        self.conv = conv
 
    def forward(self, x1, other):  # other is not used in the forward function!
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model and setting the 'other' tensor. Since this tensor won't be passed as an input to the model, it will have been trained on its own during the forward pass.
conv  = torch.nn.Conv2d(3,8,1) # Pointwise convolution with kernel size 1
other = conv.weight * 0.5 + torch.randn_like(conv.weight) * 0.01
 
m = Model(conv)


# Inputs to the model
x1 = torch.randn(1,3,64,64)
__output__  = m(x1, other=other)

