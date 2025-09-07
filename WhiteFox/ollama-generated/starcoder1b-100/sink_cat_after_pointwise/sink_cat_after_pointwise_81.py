
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ..., xn):
        v1 = torch.cat([x1, x2, ..., xn], dim=0)
        return torch.relu(v1)


# Initializing the model
m = Model()


