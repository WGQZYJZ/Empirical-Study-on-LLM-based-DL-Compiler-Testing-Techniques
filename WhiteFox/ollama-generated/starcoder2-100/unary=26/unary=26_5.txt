

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(32, 8, kernel_size=(1, 1), stride=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v0  = self.conv_transpose(x)
        mask = (v0 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2  = torch.where(mask, v0, -self.negative_slope * v0 ) 
        return v2


# Initializing the model