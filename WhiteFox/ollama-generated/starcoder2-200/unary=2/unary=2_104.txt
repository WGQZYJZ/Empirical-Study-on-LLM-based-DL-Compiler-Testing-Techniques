
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)

    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = v1 *  0.5 # multiplication 46
        v3  = v2 ** 3 # cubing 79 
        v4  = v3 * .044715 # multiply by constant 85.70887782373355
        v5  = v2 + v4 # addition 69.55545043945312 
        v6  = v5 * .7978845 # multiplication by constant 59.52329254150391
        v7  = torch.tanh(v6) # hyperbolic tangent function 59.228504638671875
        v8  = v7 +  1# addition 59.228504638671875 
        v9  = v2 * v8 # multiplication of the first input and the last output 59.228504638671875
        return v9

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # inputs for the first input to the model
__output_t1__  = m(x1)# outputs of the first input of the model. This will be used as input in the second input

