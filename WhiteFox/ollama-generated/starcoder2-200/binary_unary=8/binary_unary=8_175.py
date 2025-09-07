
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other # Add another tensor to the output of the convolution
        v2  = torch.relu(v1)        # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m2  = Model2()
 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = x1 * (-1.) # This is another input of the model
 
__output__  = m2(x1)

