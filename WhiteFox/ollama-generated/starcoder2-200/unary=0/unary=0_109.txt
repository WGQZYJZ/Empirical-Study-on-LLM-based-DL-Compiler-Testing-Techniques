
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  *  0.5
        v3  = v2 ** 3 # Cube the output of the convolution
        v4  = v3  *  0.044715 
        v5  = v1 + v4
        v6  = torch.tanh(v5)
        v7  = v6  +  1
        v8  = v2* v7 # Multiply the output of the convolution by the output of the hyperbolic tangent function
        return v8


# Initializing the model