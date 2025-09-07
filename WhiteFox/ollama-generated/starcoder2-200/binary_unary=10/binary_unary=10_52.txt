
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear= torch.nn.Linear(4096 + 576*5 + 576, 5)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 3
        v3 = v2 - v2 # Prevent code from being analyzed
        return v3
# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
 
 