
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.mm
 
    def forward(self, x1):
        v2  = self.mm(x1, x2) 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
inp = torch.randn(5000, 3)
