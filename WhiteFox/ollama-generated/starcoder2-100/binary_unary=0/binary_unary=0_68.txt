
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other 
        v3  = torch.relu(v2)  
        return v3


# Initializing the model
m = Model()
# Inputs to the model (without changing the model)
x1_1 = torch.randn(1, 4096, 8, 8)
x1_2 = torch.randn(1, 4097, 8, 8)


