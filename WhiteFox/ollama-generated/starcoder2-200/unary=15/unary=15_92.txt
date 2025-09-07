
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = torch.relu(x1)
        v1  = self.conv(v0)
        return v1
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 32, 64, 64)
