
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.convT(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution

# Initializing the model