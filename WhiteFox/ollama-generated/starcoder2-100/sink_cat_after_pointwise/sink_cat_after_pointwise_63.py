
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        v  = torch.cat([t1, t2], dim=...)
        return v.view(-1).relu()


# Initializing the model
m  = Model()
t1 = torch.rand(10)
t2 = torch.rand(10)
