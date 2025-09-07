
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.convtranspose(x) # Apply the transposed convolution to an input tensor
        v2  = torch.nn.ReLU()(v1)   # Apply the ReLU activation function to the output of the transposed convolution 
        return v2

# Initializing the model
m = Model()

