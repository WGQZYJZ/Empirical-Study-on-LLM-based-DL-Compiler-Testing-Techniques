
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1) # Apply convolution to the input tensor
        v2 = F.sigmoid(v1) # Apply sigmoid activation function to the output of the convolution 
        v3 = v1 * v2 # Multiply the output of the convolution by the output of the sigmoid activation function

# Initializing model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64) 
 __output__  = m(x1)

