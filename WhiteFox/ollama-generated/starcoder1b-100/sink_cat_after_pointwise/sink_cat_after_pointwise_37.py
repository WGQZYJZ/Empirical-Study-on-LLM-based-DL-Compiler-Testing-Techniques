
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2], dim=1)
        t2 = t1.view(t1.shape[0] // 2, -1)
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m = Model()


