
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = (v1 ** 3)
        v4   = torch.pow(v3 , 0.6708203932499369, out=None) # Apply the power function to the output of the convolution and return the result. The exponent is taken as a float.
        v5   = v1 + v4 * (1-v1) 
        v6   = v2 * 0.7978845608028653 
        v7   = torch.tanh(v6) # Apply the hyperbolic tangent function to the output of the convolution
        v8   = v7 + 1
        v9   = v8  * (1+v8)
        return v9

# Initializing the model
m = Model()

