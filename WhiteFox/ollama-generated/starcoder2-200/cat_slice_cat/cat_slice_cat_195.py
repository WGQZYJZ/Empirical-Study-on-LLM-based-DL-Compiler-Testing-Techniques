
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3,8,5)
 
    def forward(self,x1):
        return 4 * self.conv2d(x1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,3,64,64)
