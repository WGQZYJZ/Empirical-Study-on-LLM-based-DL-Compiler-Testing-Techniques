

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, x2=None):
        v  = self.mm(x1, x2)
        
        return v


m = Model()

# Inputs to the model