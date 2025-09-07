
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5    # Multiply the output of the convolution by 0.5 
        v3 = v1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
        v4 = torch.erf(v3)   # Apply the error function to the output of the convolution
        v5 = v2 * (v4 + 1)  # Multiply the output of the convolution by the output of the error function 
        return v5
# Initializing the model
m_new = Model()
# Inputs to the new model
x  = torch.randn(1,3,64,64)

