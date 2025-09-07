
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # add a constant tensor to the output of the convolution
        v3 = torch.relu(v2) # apply the ReLU activation function to the result
        return v3


# Initializing model
m  = Model()
__output_1__ = m(torch.randn(1, 3, 64, 64)) 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # other tensor
other  = x1 + torch.randn(1, 8, 12, 9)

