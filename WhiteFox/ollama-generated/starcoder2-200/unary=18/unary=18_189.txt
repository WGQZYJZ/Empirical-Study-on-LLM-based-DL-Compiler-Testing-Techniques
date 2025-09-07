
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1) # Pass the output of the convolution through a sigmoid activation function
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


# Please provide the input and output values (tensor or constant values). If the output type is int/float/bool please provide only those. The shape of each input should be provided as a tuple. Incase you have more than one output tensor, provide as a list. The output should be generated with each forward call. 
