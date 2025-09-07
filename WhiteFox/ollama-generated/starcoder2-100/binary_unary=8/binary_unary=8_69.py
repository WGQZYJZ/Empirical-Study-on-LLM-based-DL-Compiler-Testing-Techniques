
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) + x2
        v2  = torch.relu(v1)
 
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(10, 3, 8 , 8)
 
# The output of the model is assigned to a variable (__output__)
__output__= m(x1, x2)

