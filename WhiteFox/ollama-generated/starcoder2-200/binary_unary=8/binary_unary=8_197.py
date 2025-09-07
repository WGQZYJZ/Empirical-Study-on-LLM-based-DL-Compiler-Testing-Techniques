
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor # Adding another tensor to the output of the convolution
        v3  = torch.relu(v2)# Applying ReLU on the result
        return v3


# Initializing and running the model
m   = Model()
x1  = torch.randn(1, 3, 64, 64)
other_tensor  = torch.randn(1, 8, 50, 50) # Another tensor which is added to v2 by m.forward(x1).
__output__   = m(x1)

