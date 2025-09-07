
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.nn.functional.relu(v1)

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3,8,4096,)
__output__  = m(x1)

