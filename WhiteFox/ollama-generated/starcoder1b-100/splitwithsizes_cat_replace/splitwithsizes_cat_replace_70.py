
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return torch.cat((x2, v2))
 
 # Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(10, 3, 64, 64)
