
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp):
        m = torch.mm(x1, x1) + inp
        return m

# Initializing the model
m  = Model()


