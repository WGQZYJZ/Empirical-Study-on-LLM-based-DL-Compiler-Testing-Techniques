
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute((0,))
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 2).T



__output__  = m(x1)
