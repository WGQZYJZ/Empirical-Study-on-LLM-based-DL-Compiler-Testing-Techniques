
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 3)
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()


