
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.25):
        super().__init__()
        self.convTranspose1d = torch.nn.ConvTranspose1d(in_channels=3, out_channels=8, kernel_size=(64), stride=None)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.convTranspose1d(x1)
        v2  = (v1 > 0).float() 
        v3  = -v1 * self.negative_slope
        v4  = torch.where(v2==True, v1 , v3) 
        return v4

# Initializing the model
m = Model(negative_slope=0.5)
