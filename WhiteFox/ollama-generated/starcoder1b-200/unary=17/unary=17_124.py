
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v  = self.conv(x)  # Apply the transposed convolution to the input tensor
        return relu(v)


# Initializing the model
m = Model()

