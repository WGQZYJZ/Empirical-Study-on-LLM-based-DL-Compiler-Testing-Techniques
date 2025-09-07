
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2) + 0.5
        return v


# Initializing the model
m = Model()
