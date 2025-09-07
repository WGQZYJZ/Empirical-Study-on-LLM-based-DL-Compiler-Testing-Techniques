
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + t2
        v3 = torch.relu(v2)

# Initializing the model
m = Model()

# Inputs to the model
t2  = torch.randn(8, 3, 64, 64) # Another tensor which will be added to the result of pointwise convolution with kernel size 1 applied on input tensor x1 from the previous model.
x1 = torch.randn(1, 3, 64, 64)

 