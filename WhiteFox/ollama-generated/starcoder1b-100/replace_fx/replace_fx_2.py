
# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = self.apply(x1)  # Apply the fallback to the output node of the current model's graph, and then call `apply` with it.
        return t2
