
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.zeros((8))
        v[0]  = 54321.67
        return v

# Initializing the model
m  = Model()
__output__  = m()

