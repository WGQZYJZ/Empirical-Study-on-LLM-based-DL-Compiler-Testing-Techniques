
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.zeros_like(x1) + 37
        v1  = self.linear(v2)
        return v1


# Initializing the model
m = Model()
