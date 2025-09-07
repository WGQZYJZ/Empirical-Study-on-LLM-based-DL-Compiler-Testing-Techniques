
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * (-1e6 + 1)  # tanh is negative function
        return torch.where(v2 < 0, -torch.sign(v2), v2)


# Initializing the model
m = Model()

