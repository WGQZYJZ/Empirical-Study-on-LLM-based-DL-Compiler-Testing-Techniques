
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        t2 = torch.rand_like(x1)
        return t1 * t2

# Initializing the model
m = Model()


