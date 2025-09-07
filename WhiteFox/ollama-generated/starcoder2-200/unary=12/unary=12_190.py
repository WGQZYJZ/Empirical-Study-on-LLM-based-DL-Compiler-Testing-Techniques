
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # pointwise convolution with kernel size 1 to the input tensor 
        v2  = torch.sigmoid(v1) # Applying sigmoid function to the output of the convolution  
        v3  = v1 * v2 # Multiply the output of the convolution by the output of the sigmoid function
        return v3

# Initializing model
m  = Model()

# Input tensor for the model initialization (assuming that m is the model after being initialized with Model())
x1= torch.randn(1, 3, 64, 64)

# Calling model function on input tensor x1 to produce output __output__
