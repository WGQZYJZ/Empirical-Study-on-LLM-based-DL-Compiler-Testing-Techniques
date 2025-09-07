
# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 10)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1) # Apply a transposed convolution to the input tensor
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(320459, 6780, 4488)
__output__  = m(x1)
