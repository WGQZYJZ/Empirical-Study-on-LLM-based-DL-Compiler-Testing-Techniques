
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8*64*64, 5)

    def forward(self, x1):

        v2 = torch.sigmoid(v1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 8*64*64)
