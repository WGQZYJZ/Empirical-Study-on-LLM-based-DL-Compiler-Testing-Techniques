
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        v2  = self.dropout(x1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(32)


__output__  = m(x1)