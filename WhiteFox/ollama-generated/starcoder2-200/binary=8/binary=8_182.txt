
class Model(torch.nn.Module):
    def __init__(self, tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1) + kwargs['tensor']

# Initializing the model
m = Model()

 # Inputs to the model