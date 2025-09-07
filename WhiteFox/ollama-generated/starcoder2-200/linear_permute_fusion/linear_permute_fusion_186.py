
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 3)
        v2 = v1.permute(-1, -2) # Swap the last two dimensions of the tensor with shape [3]
        return v2


# Initializing the model