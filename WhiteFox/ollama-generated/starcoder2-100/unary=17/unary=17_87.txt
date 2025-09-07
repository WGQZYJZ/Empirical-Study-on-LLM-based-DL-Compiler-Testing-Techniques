
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.relu(v1) 
        return v2

# Initializing the model