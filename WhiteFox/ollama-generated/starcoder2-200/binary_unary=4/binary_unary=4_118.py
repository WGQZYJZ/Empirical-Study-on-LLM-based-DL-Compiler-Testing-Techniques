
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10,5)

    def forward(self, x1, other=None): 
        v2 = None
        v3 = None

        if other is not None:
            v2 = self.linear(x1)+other
        else: 
            v3 = self.linear(x1)
        return torch.relu(v2)


# Initializing the model and passing `other` as a keyword argument to the model.
m  = Model()
__output__  = m(torch.randn(4,10), other=torch.tensor(5))

