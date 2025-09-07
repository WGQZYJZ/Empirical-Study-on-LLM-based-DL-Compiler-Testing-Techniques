
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.addmm(x1, x1, x2)
        t2 = torch.cat([t1], dim=1)
        return t2


# Initializing the model
m = Model()


