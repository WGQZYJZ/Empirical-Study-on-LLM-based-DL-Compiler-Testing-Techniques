
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t3 = torch.relu(x1 + 1)  # Sinking operation: add constant value to the tensor
        return self._forward(t3, x2)
        
    def _forward(self, t1, x2):
        t2  = torch.cat([t1, t2], dim=...) 
        return t2


# Initializing the model
m = Model()
        
# Inputs to the model