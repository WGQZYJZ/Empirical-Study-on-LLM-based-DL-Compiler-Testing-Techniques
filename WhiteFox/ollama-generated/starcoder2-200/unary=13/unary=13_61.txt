
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(64 * 64 * 3, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1) 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(4375, 64 * 64 * 3)
__output__   = m(x1) 
