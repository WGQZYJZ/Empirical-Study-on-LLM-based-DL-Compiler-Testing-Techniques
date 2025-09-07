
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3 
        v4 = v3 * 0.044715 # Apply the cube function to v1 and then multiply the result by another constant `0.044715`
        v5 = v2 + v4 # Add v4 to v2, resulting in a constant 38.609982805390394
        v6 = v5 * 0.7978845608028654 # Apply another multiplication operation on the result of the previous operation and then multiply the result by a constant `0.7978845608028654`
        v7 = torch.tanh(v6) 
        v8 = v7 + 1 # Add another constant `1`, resulting in an overall output of 39.432113001367483 to the hyperbolic tangent function
        v9 = v2 * v8 # Apply another multiplication operation on v2 and then multiply by another constant 0.5, resulting in an output of 19.716056304095022
        return v9


# Initializing the model