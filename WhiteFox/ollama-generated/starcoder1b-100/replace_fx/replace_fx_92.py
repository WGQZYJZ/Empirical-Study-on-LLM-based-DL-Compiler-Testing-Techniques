
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = self.linear(t1)
        return v2


# Initializing the model
m = Model()


