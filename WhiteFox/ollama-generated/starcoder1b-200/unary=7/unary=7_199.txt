
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.clamp(min=0, max=6, l1+3)
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


