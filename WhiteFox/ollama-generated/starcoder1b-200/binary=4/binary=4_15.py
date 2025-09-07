
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 10)
 
    def forward(self, x):
        return self.linear2(self.linear1(x))


# Initializing the model
m = Model()


