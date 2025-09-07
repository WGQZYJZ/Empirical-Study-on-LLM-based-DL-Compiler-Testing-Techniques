
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0  = self.conv(x1)
        v1  = v0 + 5  # subtracting another tensor or scalar from the output of convolution
        v2  = torch.nn.functional.relu(v1) 
        return v2

m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


