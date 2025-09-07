
class Model(torch.nn.Module):
    def __init__(self, inp=1):
        super().__init__()
        self.m = torch.nn.Linear(3, 8)

    def forward(self, x1, input2):
        v1 = self.m(x1)
        return v1 + input2


# Initializing the model
model  = Model()

# Inputs to the model
input1 = torch.randn(100, 3, 64, 64)
inp = torch.randn(8, 3)
