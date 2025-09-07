
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x):
        v = self.linear(x)
        v2 = v * torch.sigmoid(v)
        return v2


# Initializing the model
m = Model()


