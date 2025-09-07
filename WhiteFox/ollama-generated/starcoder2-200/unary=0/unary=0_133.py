
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5 
        v3  = torch.relu((v2**4) + (torch.tensor(-27698.0))) # Apply the ReLU function to the square of the output of the convolution plus a constant -27698.0
        return v3

# Initializing the model
m  = Model()
