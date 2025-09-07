
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.negative_slope  = negative_slope

    def forward(self, x1):
        v1  = self.conv(x1)
        mask = (v1 > 0).type(torch.cuda.FloatTensor)
        v2  = torch.mul(v1, -self.negative_slope) # the negative_slope is an attribute of this model object and it is not an input argument to the forward function 
        v3  = torch.where(mask, v1, v2)
        return v3


# Initializing the model with a negative slope of 0.75:
m = Model(negative_slope=0.75)

# Inputs to the model and applying it for computing the output:
x1  = torch.randn(1, 3, 64, 64) # any random input tensor
