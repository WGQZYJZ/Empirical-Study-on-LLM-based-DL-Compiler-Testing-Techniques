
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)
        t2 = t1.view(-1, 4)
        return torch.relu(t2)


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 5)
x2 = torch.randn(1, 6, 5)
