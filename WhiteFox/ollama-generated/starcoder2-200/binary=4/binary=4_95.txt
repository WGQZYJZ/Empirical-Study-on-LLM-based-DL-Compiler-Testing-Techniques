
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768 + 10 * 4, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model (the input tensor should be of size [28, 2])
x1 = torch.randn(32768 + 40, requires_grad=True)
other = torch.randn(5, 4) * 0.5
__output__  = m(x1 + other)

