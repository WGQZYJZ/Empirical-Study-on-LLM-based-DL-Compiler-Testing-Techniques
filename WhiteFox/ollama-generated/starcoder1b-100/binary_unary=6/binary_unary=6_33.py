
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - 0.5) * 0.7071067811865476
        return torch.relu(v2)


# Initializing the model
m = Model()


