
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8,1,stride=1,padding=1)

    def forward(self,x1,**kwargs):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + kwargs["other"] 
        return v2


# Initializing the model and setting a keyword argument: other=torch.zeros((4,8))
m = Model()
m.forward(x1,other=torch.zeros(4,8))