
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.convXd(x1, 2) # X can be 1, 2, or 3 representing the dimension


# Initializing the model
m = Model()


