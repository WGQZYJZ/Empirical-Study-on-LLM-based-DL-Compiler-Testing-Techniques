
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)

    def forward(self, x):
        v1 = x.permute((0, 3, 1)) # 1 1 48  1
        v2 = torch.nn.functional.linear(v1, self.linear.weight.reshape(576, -1), self.linear.bias)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn((8, 3, 48)) # 3 48  1
__output__  = m(x).shape<jupyter_output><empty_output>