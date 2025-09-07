
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() * -5.6478393 + v1 * (-0.24152375)
        return torch.where(v2 >= 0, v1, v2)

# Initializing the model
m = Model()

