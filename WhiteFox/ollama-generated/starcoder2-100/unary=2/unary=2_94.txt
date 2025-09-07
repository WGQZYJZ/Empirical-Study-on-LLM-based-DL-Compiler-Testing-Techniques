

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5
        v3  = v1 + v1
        v4  = torch.pow(v3, -3) # Use the pow function instead of cbrt, cube root for stability purpose (e.g., in case there is a negative number input to the cbrt). If you use the torch.pow, then please also set the 'out' parameter of pow() function; Otherwise, the torch.pow is not considered as multiplication. 
        v5  = v4 + 0.044715
        v6  = v2 * v3
        __output__   = v8
        return v9


# Initializing the model
m = Model()
 
 # Inputs to the model (a fake input)
x1 = torch.randn(1, 8, 30, 45)
__output__   = m(x1)