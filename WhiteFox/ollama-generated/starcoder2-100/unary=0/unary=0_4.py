
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = (v1 * v1).sqrt() # Square root of the output of the convolution
        v4  = v3 * v1          # Cube of the output of the convolution and multiply by another constant `0.7978845608028654`
        v5  = torch.tanh(v4)
        v6  = v5 + 1           # Hyperbolic tangent function is applied to the result of the previous operation,
                                # and then 1 is added to the output of hyperbolic tangent function 
        v7  = v2 * v6          # The output of the convolution is multiplied by another constant `0.498839` and 
                               # the result is added to 0.7978845608028654
        return v7


# Initializing the model
m = Model()

