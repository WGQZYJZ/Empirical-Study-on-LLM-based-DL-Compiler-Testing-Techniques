
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.bmm(x1.permute(0, 2, 1), torch.randn(3, 5))
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 4)

