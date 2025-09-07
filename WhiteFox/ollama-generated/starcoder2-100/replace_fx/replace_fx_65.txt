
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # this is where the initial graph comes from.

        t0 = torch.nn.functional.dropout(x1, p=0.5)  # this dropout node will be replaced
        t2 = torch.rand_like(t0)
        return (None, None), {0: [t2]}

# Initializing the model
m = Model()

