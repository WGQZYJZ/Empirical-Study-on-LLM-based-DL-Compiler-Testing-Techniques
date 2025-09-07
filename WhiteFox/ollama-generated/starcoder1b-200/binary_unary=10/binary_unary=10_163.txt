
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2=None):
        return self.linear(x1).add(x2)


# Initializing the model
m = Model()


