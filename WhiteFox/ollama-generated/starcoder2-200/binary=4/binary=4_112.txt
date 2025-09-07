
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 1)

    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other
        return v2


# Initializing the model
m = Model()
other  = torch.randn([3, 1])

 # Inputs to the model (note that we need to pass a second tensor here: the other tensor)
x  = torch.randn(5, 20)
__output__  = m(x, other)
