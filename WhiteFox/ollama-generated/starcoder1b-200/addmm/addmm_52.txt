
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        if not isinstance(x2, torch.Tensor):
            x2 = torch.randn(1)
        v = torch.mm(x1, x2)
        return inp


# Initializing the model
m = Model()
