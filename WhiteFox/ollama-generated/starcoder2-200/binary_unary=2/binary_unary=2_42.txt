
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = None
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other if self.other is not None else v1
        v3 = torch.nn.ReLU()(v2)  # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v3


# Initializing the model with an initial value of a scalar for the input tensor
m = Model()

# Inputs to the model, 3 x 64 x 64. Other is set later on at run time
x1 = torch.randn(3, 32, 32) # Set this value at run time in real life scenarios
