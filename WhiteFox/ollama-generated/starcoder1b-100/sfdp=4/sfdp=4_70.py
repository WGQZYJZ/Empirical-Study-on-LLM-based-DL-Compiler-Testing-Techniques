
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer 1 = Conv()
        self.layer 2 = Conv()

    def forward(self, x1):
        v1 = self.layer 1(x1)
        v2 = self.layer 2(x1)
        return v1 + v2


# Initializing the model
m = Model()

