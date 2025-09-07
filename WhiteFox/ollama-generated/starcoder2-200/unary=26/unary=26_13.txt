
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
    
    def forward(self, x1):
        v1 = self.conv(x1)
        mask  = (v1 > 0).type_as(negative_slope) # Mask where True indicates elements greater than 0
        negative_slope = torch.full_like(mask, negative_slope)
        v3 = torch.where(mask, v1, v1*negative_slope)
        
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
