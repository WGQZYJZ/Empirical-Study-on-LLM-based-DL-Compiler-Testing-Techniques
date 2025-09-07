
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1: Tensor):
        v = torch.mm(x1, x2)
        return v + inp


m = Model()
