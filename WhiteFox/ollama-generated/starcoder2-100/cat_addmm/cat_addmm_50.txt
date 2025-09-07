
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.conv = torch.nn.Linear(input1, 3)
        
    def forward(self, x1, x2):
        v1  = self.conv(x1)
        v4  = x2
        t0   = v1 + v4
        return t0
        
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(64, 4)
x2 = torch.randn(3, 8, 8)
__output__  = m(x1, x2)