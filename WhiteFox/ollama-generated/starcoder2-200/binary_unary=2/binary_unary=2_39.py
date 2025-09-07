
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1) - self.__other__
        v2  = torch.relu(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Outputs from the model
__output_0__,  __other__ = m(x1)

 