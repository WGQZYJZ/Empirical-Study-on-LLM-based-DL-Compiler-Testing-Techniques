
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.convT(x) # Apply pointwise transposed convolution to the input tensor
        v1 = torch.sigmoid(v0) # Apply the sigmoid function to the output of the transposed convolution
        return v1

# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)

