
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = v1 - t
        v3  = F.relu(v2) # Apply ReLU function to the result
        return v3


# Initializing the model:
m = Model()


# Inputs to the model:
t = torch.randn(1, 8, 64, 64)
x1 = torch.randn(1, 3, 64, 64)
__output__= m(x1)


