

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1 = v0 - other
        v2 = torch.relu(v1)

# Initializing the model
m = Model()

 # Inputs to the model
__input_x__, __input_other__  = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 50, 20)
__output__  = m(__input_x__, __input_other__)
