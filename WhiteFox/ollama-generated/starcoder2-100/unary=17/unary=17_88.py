
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.relu(v1) # Applying ReLU activation function to the transposed convolution output
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 

# Expected output from the model with the provided inputs and weights
__output__  = m(x1)

