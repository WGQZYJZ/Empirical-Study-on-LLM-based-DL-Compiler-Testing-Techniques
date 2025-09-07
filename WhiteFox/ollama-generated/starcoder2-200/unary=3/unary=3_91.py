
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1  + 1.4 # Modify the existing code
        v4  = torch.relu6(v3) 
        v5  = v4 / 3.9  # Modify the existing code
        v6  = v2 * v5
        return v6

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

