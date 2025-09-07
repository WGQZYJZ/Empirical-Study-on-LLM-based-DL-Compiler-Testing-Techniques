
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor 
        v2  = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3  = v2 ** 3 # Square the output of the convolution (the result is a tensor)  
        v4  = torch.pow(v3, -6) # Raise to the power of `-6` 
        v5  = v1 + v4 # Add the output of the convolution and the result of the previous operation
        v6  = v2 * 0.7978845608028654 # Multiply the output of the convolution by another constant `0.7978845608028654` 
        v7  = torch.tanh(v1 + 1) * v3 - 5 / (torch.expm1(-v1) - v1) # Apply hyperbolic tangent function to the output of the convolution, multiply by the power of the output of the previous operation, and then subtract another constant `-5`
        return torch.sum(v7)


# Initializing the model 
m = Model() 

# Inputs to the model
x1  = torch.randn(2 ,3 ,64 ,64 )
 
 