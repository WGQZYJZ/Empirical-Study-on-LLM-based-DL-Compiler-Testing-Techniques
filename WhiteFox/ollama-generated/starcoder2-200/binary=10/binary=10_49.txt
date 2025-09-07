
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()
other  = torch.randn([1])

 # Inputs to the model
x2 = torch.randn(3*64*64)
__output__  = m(x2)

