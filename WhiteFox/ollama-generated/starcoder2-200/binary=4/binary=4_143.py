
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.Linear(2048 * 3 + 64*64)(x)
        v2 = v1 + torch.randn_like(v1)
        return v2


# Initializing the model and the input tensor to feed in the model