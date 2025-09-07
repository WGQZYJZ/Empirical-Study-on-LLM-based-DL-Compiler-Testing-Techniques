
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2048, 10)
        self.linear2 = torch.nn.Linear(10, 10)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1 + x1)
        return v2


# Initializing the model
m = Model()


