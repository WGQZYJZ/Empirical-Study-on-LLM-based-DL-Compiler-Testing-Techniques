
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.where(v1 > 0, x1, -v1)


# Initializing the model
m = Model()

