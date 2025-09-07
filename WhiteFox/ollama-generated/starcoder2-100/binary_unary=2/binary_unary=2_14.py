
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 - other 
        v4  = torch.relu(v2)
        return v4

 # Initializing the model
m = Model()

# Inputs to the model
other  = torch.randn(1,3,64,64)
x  = torch.randn(1,3,64,64)

