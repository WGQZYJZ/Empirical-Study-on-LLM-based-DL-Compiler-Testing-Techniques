
class Model(torch.nn.Module):
    def __init__(self, n_units):
        super().__init__()
        self.linear1 = torch.nn.Linear(n_units, n_units // 2)
        self.linear2 = torch.nn.Linear(n_units // 2, n_units // 2)
 
    def forward(self, x):
        return self.linear1(x).view(-1, 10).addmm(self.linear2, x.view(-1, 10)).view(x.shape[0], -1)


# Initializing the model
m = Model(n_units=64)


# Inputs to the model
x = torch.randn(10, 64)
