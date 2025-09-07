
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
    
    def forward(self, x):
        v1  = F.conv_transpose2d(x, self.conv) # Apply pointwise transposed convolution to the input tensor
        v2  = v1.clamp(max=255) # Clamp the output of the transposed convolution to a maximum value (constant is 255 here.)
        return v2

# Initializing the model
m = Model()

