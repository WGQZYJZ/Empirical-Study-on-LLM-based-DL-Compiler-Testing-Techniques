
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = self.conv2d(x1)
        return v1 + other if other is not None else v1

 # Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(500, 3, 64, 64)
