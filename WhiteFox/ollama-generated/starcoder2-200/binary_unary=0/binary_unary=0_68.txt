
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.bn    = torch.nn.BatchNorm2d(8)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 4 # We add another constant tensor (4 here in this case) to the output of the convolution
        v3  = self.bn(v2) 
        v4  = self.relu(v3)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1) # The model should be able to produce the same result as before if the input is not changed

