
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v3 = relu(v1 - other_constant)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(4).to('cuda')
__output__  = m(x2)
