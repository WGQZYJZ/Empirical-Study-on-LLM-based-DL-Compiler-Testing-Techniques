
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        return torch.bmm(v1, x2)


# Initializing the model
m = Model()
__output_tensor__ = m(x1, x2) # or 