
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.sigmoid(v1)  # Apply sigmoid function to the output of the convolution 
        v3  = v1 * v2   # Multiply the output of the convolution by the output of the sigmoid activation function.
        return v3

# Initializing the model: 
m = Model()

