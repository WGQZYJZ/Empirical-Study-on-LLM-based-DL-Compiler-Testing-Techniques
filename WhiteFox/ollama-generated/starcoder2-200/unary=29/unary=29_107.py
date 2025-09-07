
class Model(torch.nn.Module):
    def __init__(self, minv = 0., maxv =1):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3,8, kernel=3)
        self.maxv = maxv
        self.minv = minv
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = torch.clamp_min(v1, self.minv) 
        v3  = torch.clamp_max(v2 , self.maxv) 
        return v3


m = Model() # Initialize the model using provided values for the minimum and maximum values as keyword arguments
 
 x1 = torch.randn(1, 3, 64, 64) 
