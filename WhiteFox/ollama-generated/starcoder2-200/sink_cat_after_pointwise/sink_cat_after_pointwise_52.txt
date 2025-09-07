
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        t0  = torch.cat([x1, y1], dim=1)
        t1  = t0.view(-1, ) # Re-shape the concatenated tensor
        t2  = torch.relu(t1)
        return t2


# Initializing the model
m  = Model()
