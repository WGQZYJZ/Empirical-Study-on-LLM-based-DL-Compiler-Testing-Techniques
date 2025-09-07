
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 3)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            return v1
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

