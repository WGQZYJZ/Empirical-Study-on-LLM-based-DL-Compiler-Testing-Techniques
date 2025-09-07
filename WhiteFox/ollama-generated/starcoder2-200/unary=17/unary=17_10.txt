
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.activation = torch.nn.ReLU()
 
    def forward(self, x1): 
        v1  = self.convT(x1) # Apply a transposed convolution to the input tensor
        v2  = self.activation(v1) # Apply ReLU activation function to the output of the transposed convolution 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)