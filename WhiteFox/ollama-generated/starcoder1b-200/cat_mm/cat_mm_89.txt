
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, *args):
        res = torch.mm(x1, x2)
        return res


# Initializing the model
m = Model()


