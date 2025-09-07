
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(v1 + 3, l1=0, l2=6)
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


