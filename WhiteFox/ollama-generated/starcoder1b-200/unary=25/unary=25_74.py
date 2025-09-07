
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2 = torch.where(v1 > 0, v1, negative_slope * v1)
        return v2


# Initializing the model
m = Model()


