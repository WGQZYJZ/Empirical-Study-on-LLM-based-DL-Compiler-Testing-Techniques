
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 * (-1 + (v1 * 0.75).pow_(2))


# Initializing the model
m = Model()


