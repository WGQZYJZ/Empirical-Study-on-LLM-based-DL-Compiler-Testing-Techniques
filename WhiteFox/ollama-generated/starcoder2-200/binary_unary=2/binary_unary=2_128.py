
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Conv2d(3, 8, 1)(x1) - self._conv_weight
        v2 = F.relu(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model