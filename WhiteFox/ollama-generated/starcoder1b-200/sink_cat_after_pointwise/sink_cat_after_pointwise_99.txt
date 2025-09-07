
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        ...  # ...
        return t3  # Return only the tensor 't3' as output for later optimization


# Initializing the model
m = Model()


