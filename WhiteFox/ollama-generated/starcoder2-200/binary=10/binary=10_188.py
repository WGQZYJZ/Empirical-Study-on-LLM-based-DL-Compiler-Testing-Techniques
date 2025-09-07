
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=0.5): 
        v2  = self.conv(x1) # The input tensor is the output of a pointwise convolution in the model class
        v4  = torch.erf(v3) * other # The third tensor `other` is an additional input to the model. 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
