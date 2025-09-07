
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, 10) + self.conv(inp) 
        return v6

 # Initializing the model
m  = Model()
 
 # Inputs to the model