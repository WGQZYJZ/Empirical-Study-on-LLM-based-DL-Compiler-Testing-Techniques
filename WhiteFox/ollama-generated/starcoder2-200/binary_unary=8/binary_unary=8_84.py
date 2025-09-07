
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8,1)

    def forward(self,x):
        v1  = self.conv1(x)
        v2  = v1 + x
        return nn.functional.relu(v2)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3,64,64)

__output__  = m(x).shape

