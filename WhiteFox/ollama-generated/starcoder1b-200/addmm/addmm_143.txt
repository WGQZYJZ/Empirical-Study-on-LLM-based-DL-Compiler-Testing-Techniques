
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        y = torch.mm(x1, inp)
        return y


# Initializing the model
m = Model()


