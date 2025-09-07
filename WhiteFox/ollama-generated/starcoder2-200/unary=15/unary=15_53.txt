
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.ReLU()(self.conv)  # Apply the ReLU activation function to the output of the convolution 
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 28, 28)
__output__  = m(x1)


