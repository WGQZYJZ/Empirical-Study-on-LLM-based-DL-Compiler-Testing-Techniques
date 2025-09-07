
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1): 
        v1  = self.deconv(x1) # Apply the pointwise transposed convolution to an input tensor
        v2  = torch.relu(v1) # Apply the ReLU activation function to the output of the transposed convolution
        return v2
 
# Initializing the model
m  = Model()

 # Inputs for the model
x1  = torch.randn(1,3,64,64)

