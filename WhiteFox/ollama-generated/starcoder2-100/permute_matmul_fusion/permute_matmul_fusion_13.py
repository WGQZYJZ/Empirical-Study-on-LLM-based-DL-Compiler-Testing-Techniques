
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2): # NOTE: here, x1 and y2 are input tensors with different names.
        v0 = x1  + 5
        v1 = y2 / 3
        v2 = v0.permute(-1, -2) * v1.permute(-1, -3)
        return torch.bmm(v2, 4), v2


# Initializing the model