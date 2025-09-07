
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.m     = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 # create boolean mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise.
        v3  = negative_slope * torch.ones_like(v1) # set a constant to be the negative slope.
        v4  = self.m(torch.where(v2, v1, v3)) 
        return v4


# Initializing model
m = Model()


x1 = torch.randn(5, 3, 64, 64) # Input data

__output__  = m(x1)


