
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.25, self.training)
        v2 = torch.rand_like(x1, ...)
        return v2


# Initializing the model
m = Model()


