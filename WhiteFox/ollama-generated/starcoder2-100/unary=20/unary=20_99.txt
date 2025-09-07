
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.convtranspose(x) # Apply a pointwise transposed convolution to the input tensor
        v2  = torch.sigmoid(v1)# Apply the sigmoid function to the output of the transposed convolution
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 3, 50, 50) # Initialize input tensor

__output__  = m(x)

