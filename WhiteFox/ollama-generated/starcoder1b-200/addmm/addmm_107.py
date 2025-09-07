
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=0):
        v1 = torch.mm(x1, self.conv)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()


