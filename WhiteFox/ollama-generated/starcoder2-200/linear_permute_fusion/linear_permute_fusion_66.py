
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2 = v1.permute(0, 3, 1, 4) # Note that this permuation does not meet the requirement
        return v2


# Initializing the model