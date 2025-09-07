
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) - x2 # Subtract "x2" from the result of the convolution with a kernel size of 1 on the input tensor
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

