
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):
       v1   = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
       v2   = v1*0.5 # Multiply the output of the convolution by 0.5
       v3   = v1*0.7071067811865476 #Multiply the output of the convolution by 0.7071067811865476
       v4   = torch.erf(v3) # Apply the error function to the output of the convolution 
       v5   = v4 + 1 # Add 1 to the output of the error function
       v6   = v2 * v5 # Multiply the output of the convolution by the output of the error function
       return v6

# Initializing the model
m  = Model()


# Inputs to the model.
x1  = torch.randn(1,3,64,64)

