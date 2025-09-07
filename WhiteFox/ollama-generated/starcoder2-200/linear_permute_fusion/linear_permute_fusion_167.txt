
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1.permute(0, 3, 1, 2).reshape(-1, 5, 64) # swap 1 and 3 dimensions of output tensor
        return v2


# Initializing the model