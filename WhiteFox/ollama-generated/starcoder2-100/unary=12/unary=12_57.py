
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):
        v0 = x1 # Save the input tensor to a variable for easier access and debugging purposes
        v1  = self.conv(v0) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.sigmoid(v1) # Apply sigmoid function to the output of the convolution
        v3 = v1 * v2 # Multiply the output of the convolution by the output of the sigmoid function
        return v0, v1, v2, v3


# Initializing the model