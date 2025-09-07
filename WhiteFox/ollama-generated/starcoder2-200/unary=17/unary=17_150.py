
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v0 = F.relu(x1) # Apply the ReLU activation function to the input tensor
        v1  = self.convT(v0) 
        return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 32, 64, 64) # Initialize the input tensor
__output__  = m(x1)

