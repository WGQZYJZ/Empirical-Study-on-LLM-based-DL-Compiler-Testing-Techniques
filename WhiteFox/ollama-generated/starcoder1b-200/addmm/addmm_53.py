
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.tensor([[0.5]])

    def forward(self, x1, inp):
        return self.t1[0][0] + inp


# Initializing the model
m  = Model()


