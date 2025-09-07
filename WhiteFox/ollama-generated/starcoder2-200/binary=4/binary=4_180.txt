

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 + other # ADDITION OF ANOTHER TENSOR TO THE OUTPUT
        return v3


# Initializing the model
m = Model()
other = torch.randn([4, 5])


# Inputs to the model
x1 = torch.randn(4, 2048)
__output__  = m(x1)
