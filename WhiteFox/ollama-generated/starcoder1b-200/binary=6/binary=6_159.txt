
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
 
    def forward(self, x1):
        return self.linear(x1 - 2)


# Initializing the model
m = Model()
