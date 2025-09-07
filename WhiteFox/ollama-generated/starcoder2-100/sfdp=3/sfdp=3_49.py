
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v0 = torch.randn(4,64,64) # Initialize a tensor 
        v1 = self.conv(x1)
        v2 = v1 * 50 # Multiply the output of the convolution by 50 
        v3 = v1 * 98.76 # Multiply the output of the convolution by 98.76
        v4 = torch.erf(v3) + x1*x2*v4
        v5 = v1 + v2 # Add the output of the convolution to the result of multiplying a tensor with itself 
        v6 = v0 * v5 / torch.sum(v1)  # Multiply the output of the convolution by its sum, and then divide it by the sum of the output of the convolution
        return v4


# Initializing the model: 
m  = Model() 


# Input to the model (for m):
x1  = torch.randn(1,3,64,64)
x2  = x1 *0 

__output__  = m(x1)
