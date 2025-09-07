
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.functional.linear
 
    def forward(self, x1, inp=None):
        v1  = self.mm(x1) 
        return v1


# Initializing the model