
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmult = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v2 = torch.mm(x1[0], x1[0]) + self._inp
        return v2

# Initializing the model with an input tensor for keyword argument 'inp' to be added after performing matrix multiplication operation.
inp  = torch.randn(784)
m  = Model(_inp=inp)


# Inputs to the model
x1  = [torch.randn(64, 28 * 28), inp]
__output__  = m(x1)
