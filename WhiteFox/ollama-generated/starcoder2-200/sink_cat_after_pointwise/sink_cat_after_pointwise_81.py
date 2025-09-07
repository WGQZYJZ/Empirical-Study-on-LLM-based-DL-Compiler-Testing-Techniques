
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # shape = (N1, C1) where N1 > 1
        t3  = torch.relu(x1) + 100


# Initializing the model
m = Model()


# Inputs to the model
N1, C1  = 5, 20 # shape = (N1, C1) where N1 > 1
x1 = torch.randn(N1, C1)

