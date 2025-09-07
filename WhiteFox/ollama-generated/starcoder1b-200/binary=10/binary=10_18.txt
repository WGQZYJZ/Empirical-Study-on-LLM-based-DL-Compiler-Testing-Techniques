
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 64)
 
    def forward(self, x1, other=0.5):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1 + other)
        return v2


# Initializing the model
m = Model()
