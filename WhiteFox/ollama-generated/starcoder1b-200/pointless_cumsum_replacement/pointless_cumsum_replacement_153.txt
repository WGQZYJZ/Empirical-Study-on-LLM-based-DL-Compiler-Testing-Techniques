
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.full([x1.shape[0], x1.shape[1]], 1, device=device, dtype=dtype)


# Initializing the model
m = Model()


