
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 1) 
        self.leakyrelu = nn.LeakyReLU(negative_slope=negative_slope)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1)        
        v2 = (v1 > 0).float()       
        v3 = v1 * negative_slope
        v4 = torch.where(v2 == False, v3, v1)      
        return v4

# Initializing the model