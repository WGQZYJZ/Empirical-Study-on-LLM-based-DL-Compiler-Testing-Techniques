
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
 
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0) 
        self.leakyrelu  = nn.LeakyReLU(negative_slope=negative_slope)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        # Apply the leaky relu
        mask  = (v1 > 0).bool()
        out  = torch.where(mask, v1, -0.2 * v1)
        
        return out
# Initializing the model