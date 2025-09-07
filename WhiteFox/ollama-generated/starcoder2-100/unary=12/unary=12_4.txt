
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v01  = x  # The input tensor passed to the model is available as x
        v1  = self.conv(v01) 
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x_input = torch.randn(5, 3, 64, 64)

__output__  = m(x1)  # Forward pass of the model on the input tensor x1
__output__  = m(x2)  # Forward pass of the model on the input tensor x2

