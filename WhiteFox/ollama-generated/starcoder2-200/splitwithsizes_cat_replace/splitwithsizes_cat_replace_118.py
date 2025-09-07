
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.split
        self.cat  = torch.cat

    def forward(self, x1):
        v10523  = [v10489 for v10489 in self.split(x1, split_sizes=3) if (v10476 := [i for i in self._parameters().keys()])]
        __return__  = self.cat([v10524[v10480] for v10480, v10524 in enumerate(v10523)], dim=self.__dict__["dim"])


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(96)
__output__  = m(x1)
