
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.nn.Linear(1, 2)
 
    def forward(self, inp):
        v1 = torch.mm(inp, inp)
        return v1 + inp


# Initializing the model
m = Model()


