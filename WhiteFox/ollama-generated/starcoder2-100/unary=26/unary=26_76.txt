
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()

        self.convt = torch.nn.ConvTranspose2d(3, 8, (10,), stride=(5,))
        self.relu  = torch.nn.LeakyReLU(negative_slope)
 
    def forward(self, x):
        v1  = self.convt(x) 
        v2  = v1 > 0 
        v3  = v1 * -1
        v4  = torch.where(v2, v1, v3 )
        return v4

 # Initializing the model
negative_slope  = .5
m  = Model(negative_slope)
# Inputs to the model
x1   = torch.randn(10, 8, 79 , 79) 
__output__  = m(x1)

