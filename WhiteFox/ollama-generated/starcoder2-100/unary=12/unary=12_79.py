
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
        v0 = F.relu(x1) # Apply the ReLU activation function to the input tensor
        v1 = self.conv(v0) # Apply pointwise convolution with kernel size 1 on the output of the ReLU activation function
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the convolution
        v3 = v1 * v2 # Multiply the output of the convolution by the output of the sigmoid function 
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)  
__output__  = m(x1)

