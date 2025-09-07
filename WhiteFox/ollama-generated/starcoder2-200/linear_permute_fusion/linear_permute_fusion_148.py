
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight, bias=None)
        v2 = v1.permute(0, 2, 1) # swap the last two dimensions of this tensor

        return v2


# Initializing the model