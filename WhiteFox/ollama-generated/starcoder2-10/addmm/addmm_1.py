
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp):
        v1 = torch.mm(*[inp], *[1]) # perform matrix multiplication on two input tensors
        v2  = v1 + self.conv(v1)  # multiply the result of the matrix multiplication by another tensor
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model, and an additional input, 'inp', that is not used in the forward function of the model class.
x1 = torch.randn(3)
x2  = torch.randn(3)
inp = torch.randn(3) # An additional input that will be passed as a keyword argument to torch.mm()
