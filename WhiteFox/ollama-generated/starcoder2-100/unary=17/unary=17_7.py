
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.convT(x1) # Transposed pointwise Convolution (convTranspose2d())
        v2  = nn.ReLU()(v1) # Activation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)