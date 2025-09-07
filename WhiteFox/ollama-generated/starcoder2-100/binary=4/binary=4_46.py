
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 35)

    def forward(self, x1):
        v1  = self.linear(x1)
        return v1 + other

# Initializing the model
m  = Model()
other  = torch.randn([35])


# Inputs to the model
x1   = torch.randn(4, 20)
__output__  = m(x1)