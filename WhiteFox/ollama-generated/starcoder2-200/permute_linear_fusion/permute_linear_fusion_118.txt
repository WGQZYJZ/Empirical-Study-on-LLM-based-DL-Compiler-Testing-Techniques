
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v2 = torch.nn.functional.linear(x1, self.weight)
        return v2


# Initializing the model