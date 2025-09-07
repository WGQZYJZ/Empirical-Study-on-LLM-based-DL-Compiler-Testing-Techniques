
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        return self.linear(x) - 1.5


# Initializing the model
m = Model()


