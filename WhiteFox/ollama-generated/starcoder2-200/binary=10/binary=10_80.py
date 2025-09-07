
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 1)
 
    def forward(self, x):
        v2 = torch.randn(49).reshape(7, 7)
        v6 = v2 + other # add a random tensor to the output of the linear transformation
        return self.linear(v6)


# Initializing the model
m  = Model()
other = torch.rand(30,) / -1
__output__  = m(torch.randn(49).reshape(7, 7))