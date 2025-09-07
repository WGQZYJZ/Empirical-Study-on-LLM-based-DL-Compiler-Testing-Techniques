
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        v0 = torch.mm(x1, x2) + torch.mm(x3, x4) # Matrix multiplication between x1 and x2 plus matrix multiplication between x3 and x4
        return v0

# Initializing the model 
m = Model()

