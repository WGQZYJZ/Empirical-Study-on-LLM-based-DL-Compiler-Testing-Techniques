
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(64 * 64, 128)
 
    def forward(self, x1, inp=None):
        v1 = self.mm(x1).view(-1) + inp
        return v1


# Initializing the model
m = Model()
