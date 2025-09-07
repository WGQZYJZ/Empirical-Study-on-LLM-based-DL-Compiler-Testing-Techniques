
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1) 
        v2 = F.relu(v1) # Apply the ReLU activation function to the output of the transposed convolution
        return v2


# Initializing the model
m  = Model()
 

# Inputs to the model
x1 = torch.randn(3,8,64,64)
__output__  = m(x1)


