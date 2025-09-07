
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, t1, t2):
        v1  = torch.cat([t1, t2], dim=1)
        v2  = v1.view([-1, 4])
        return self.relu(v2)


# Initializing the model
m = Model()

# Input to the model
x = torch.randn(5, 100)
