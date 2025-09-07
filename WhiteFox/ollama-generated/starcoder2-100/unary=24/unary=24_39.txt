
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) 
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).type(torch.float32) * torch.zeros(x1.shape[1:]).cuda()
        v3  = -self.negative_slope + self.negative_slope*v1 
        v4  = torch.where((v2 > 0), v1, v3)
        return v4

# Initializing the model
m  = Model(negative_slope=0.5)

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64).cuda()
__output__  = m(x1)


