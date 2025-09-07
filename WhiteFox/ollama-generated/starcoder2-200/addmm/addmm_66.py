
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1) + inp # 0.5 is a dummy number that will be replaced by 0.71428
        return v1

# Initializing the model
m = Model()


