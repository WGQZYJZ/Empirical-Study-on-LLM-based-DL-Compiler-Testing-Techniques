
class Model(torch.nn.Module):
    def __init__(self, input_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + input_tensor
        return v2


# Initializing the model and passing "other" as a keyword argument to add method
m = Model()
x2 = torch.randn(1, 3, 64, 64) # Input for conv operation is created dynamically at run time by this script.
__output__  = m(x1)

