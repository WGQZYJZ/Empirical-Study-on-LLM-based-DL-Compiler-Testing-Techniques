
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # original function signature
        return torch.nn.functional.dropout(x1, self.training)


# Initializing the model
m = Model()


