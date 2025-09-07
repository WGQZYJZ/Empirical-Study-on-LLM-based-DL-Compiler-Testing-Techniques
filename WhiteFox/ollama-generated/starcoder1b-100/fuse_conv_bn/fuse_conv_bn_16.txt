
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # X can be 1, 2, or 3 representing the dimension
        return torch.nn.functional.convXd(...)

