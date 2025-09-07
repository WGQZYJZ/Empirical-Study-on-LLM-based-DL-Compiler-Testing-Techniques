
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._conv(x1) # Replace the Conv2d() function in the model
        v3 = torch.relu(v1 + self.other) 
        return v3

# Initializing the model
m  = Model()


# Inputs to the model