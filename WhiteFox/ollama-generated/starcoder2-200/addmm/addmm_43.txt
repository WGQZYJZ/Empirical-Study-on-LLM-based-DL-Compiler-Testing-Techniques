
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, inp=0.5): # add 1. to the matrix multiplication
        v2  = self.mm(x1) + inp

# Initializing the model