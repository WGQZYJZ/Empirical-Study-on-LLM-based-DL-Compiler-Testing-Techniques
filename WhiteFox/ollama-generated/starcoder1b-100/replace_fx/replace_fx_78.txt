
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        self.x1 = torch.rand_like(x1, 100)
        return torch.nn.functional.dropout(self.x1, p=0.3, training=True)


# Initializing the model
m = Model()
