
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.clamp_min(v1, min_value=0.5) 
        v3 = torch.clamp_max(v2, max_value=84.79)  
        return v3


# Initializing model 
m = Model()

# Input to the model (different from the previous input)
x1 = torch.randn(10, 3, 543, 644)
