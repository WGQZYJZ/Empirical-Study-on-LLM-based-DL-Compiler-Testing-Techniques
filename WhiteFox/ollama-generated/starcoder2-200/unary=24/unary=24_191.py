
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) 
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)  
        v2  = (v1 >  0).float() * 0.5 
        v3  = torch.ones_like(v1)
        v4  = v3 - v2 * self.negative_slope   
        v5  = torch.where((v1 >= 0).float(), v1, v4)  
        return v5


# Initializing the model
m  = Model()


 # Inputs to the model