
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
        self.ReLU = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.convT(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = self.ReLU(v1)# Apply ReLU activation function to the output of the transposed convolution
        return v2

# Initializing model
m  = Model()


# Inputs to the model