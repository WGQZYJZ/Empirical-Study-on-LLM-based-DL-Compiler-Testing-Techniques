
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x): 
        v1  = self.convT(x) # Apply pointwise transposed convolution to an input tensor
        v2  = torch.relu(v1) # Apply ReLU (Rectified Linear Unit) activation function to the output of the transposed convolution
        return v2


# Initializing the model
m = Model()

# Input for the model
x  = torch.randn(5, 3, 64, 64)

 # Compute model output
 