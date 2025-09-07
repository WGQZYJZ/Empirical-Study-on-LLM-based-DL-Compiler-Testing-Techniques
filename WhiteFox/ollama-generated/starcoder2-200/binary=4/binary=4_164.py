
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self.__other__
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(64, 784)


# Initializing another tensor (not included in the original code snippet).
other = torch.tensor([5])


__output__  = m(x)
