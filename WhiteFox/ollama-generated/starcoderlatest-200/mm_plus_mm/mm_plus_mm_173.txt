
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(512, 64)
        self.add = torch.nn.Add()
 
    def forward(self, x1):
        v1 = self.mm(x1)
        v2 = self.add(v1, v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(512, 512)
