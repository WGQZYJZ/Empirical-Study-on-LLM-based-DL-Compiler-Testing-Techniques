
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.negative_slope = negative_slope
    
    def forward(self, x):
        v1 = self.conv(x)
        mask = (v1 > 0).float()
        
        v4 = self.negative_slope * ((-mask) + 1) * (-torch.sign(v1))
        v2 = torch.where((v1 > 0).bool(), v1, v4 )
        return v2


# Initializing the model
m = Model(negative_slope=0.5)


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
__output__  = m(x)