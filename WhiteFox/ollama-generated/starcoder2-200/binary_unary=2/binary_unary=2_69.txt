
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 - other # Subtracts another tensor or scalar from the output of the convolution
        return torch.nn.functional.relu(v2)


# Initializing the model
m  = Model()


# Inputs to the model
other_tensor = torch.randn(1,3,64,64) # Other tensor
x1  = torch.randn(1, 3, 64, 64)       # Input data of shape (batch size=1, number of input channels=3, height=64 pixels and width=64 pixels)
__output__  = m(other_tensor)

