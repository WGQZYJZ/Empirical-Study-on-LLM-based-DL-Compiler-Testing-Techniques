
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, bn=True):
        if bn:
            v = torch.nn.functional.batch_norm(x1)
        else:
            v = x1
        return v


# Initializing the model
m = Model()


