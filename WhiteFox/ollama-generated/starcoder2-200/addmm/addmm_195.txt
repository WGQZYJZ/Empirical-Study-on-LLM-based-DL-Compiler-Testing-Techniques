
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._m = torch.nn.Linear(10, 10)

    def forward(self, x):
        v1 = torch.mm(x, x[:, None])
        return self._m(v1).sum()


# Initializing the model
m = Model()

# Inputs to the model
inp  = torch.randn(32, 50)
x   = torch.randn(8, 10) # 8 is the batch size here and 10 is the number of features in each example.
__output__  = m(x)

