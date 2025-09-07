
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convT(x1) # Pointwise transposed convolution operation on an input tensor
        v2 = torch.sigmoid(v1) # Sigmoid activation function applied to the output of the transposed convolution 
        return v2


# Initializing the model
m  = Model()
 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


# Expected output
output  = m(x1)

