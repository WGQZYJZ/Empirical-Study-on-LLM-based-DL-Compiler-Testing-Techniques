
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(4*4*8,100)
 
    def forward(self, x1):
        v1  = conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3 = v1* 0.7071067811865476  #Multiply the output of the convolution by 0.7071067811865476
        v4 = torch.erf(v3) # Apply the error function to the output of the convolution
        v5 = v4 + 1# Add 1 to the output of the error function
        v6 = v2* v5  #Multiply the output of the convolution by the output of the error function

        l1 = linear(v6) # Apply linear transformation to the output tensor of the multiplication
        l2 = l1 * clamp(min=0, max=6, l1 + 3)# Multiply the output of the linear transformation by the clamped output (clamped between 0 and 6) of the linear transformation added with `3`
        l3 = l2 / 6 # Divide the output of the multiplication by `6`

        return l3

# Initializing model
m = Model()


# Inputs to the model