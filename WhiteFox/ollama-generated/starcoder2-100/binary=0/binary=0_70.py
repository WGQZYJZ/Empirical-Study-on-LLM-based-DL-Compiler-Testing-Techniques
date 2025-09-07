
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, other=0.5):
        v1 = self.conv(x1)
        v2 = v1 + other # Add the other tensor to the output of the convolution 
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn(1,3,64,64), 0.5)

