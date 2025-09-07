
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1, kernel=None, stride=None, padding=0)
        v3  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        return v3 * v1
 
# Initializing the model
m  = Model()


Inputs to the model:

x1 = torch.randn(1, 256, 14, 14)


Outputs from the model:

