
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1,stride=1)
 
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
       v1  = self.conv(x1)
 
       # mask to create the required output of convtranspose operation
       v2  = torch.empty(v1.shape).fill_(0.)
       v3  = v1 > v2
       v4  = v1 * -self.negative_slope
 
       v5  = torch.where(v3, v1, v4)
 
       return v5


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(20,8,64,64)
__output__  = m(x1)


