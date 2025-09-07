
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, 2 * x1], dim=0)
        t2 = t1.view(t1.size(0), -1)
        t3 = torch.relu(t2)
        return t3

# Initializing the model
m = Model()


