
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(16, 8)
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) + x1
        return v1


# Initializing the model
m = Model()

