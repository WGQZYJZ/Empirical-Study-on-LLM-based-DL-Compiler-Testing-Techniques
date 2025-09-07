
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)

    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor 
        v2  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        return v2


# Initializing the model