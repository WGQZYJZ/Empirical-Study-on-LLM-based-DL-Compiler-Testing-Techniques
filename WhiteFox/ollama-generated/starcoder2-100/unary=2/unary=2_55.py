
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1) #Apply pointwise transposed convolution to the input tensor
        v2  = v1 * 0.5
        v3  = v1 * v1 * v1 
        v4  = v3 * 0.044715 
        v5  = v1 + v4
        v6  = v5 * 0.7978845608028654
        v7  = torch.tanh(v6) #Apply the hyperbolic tangent function to the output of the multiplication
        v8  = v7 + 1 
        v9  = v2 * v8 
        return v9

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)


# Outputs of the model on the inputs
__output__  = m(x1)