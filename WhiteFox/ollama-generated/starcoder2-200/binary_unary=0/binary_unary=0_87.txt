
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        return torch.relu(v2)


# Initializing the model and defining the input tensor.
m  = Model()
other = torch.randn(50,8,64,64)

x1  = torch.randn(3,50,64,64)
 
__output__  = m(x1)

