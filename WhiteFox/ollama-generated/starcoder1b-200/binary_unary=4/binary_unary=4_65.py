
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x1, other=0):
        v1 = self.linear(x1) + other
        return v3


# Initializing the model
m = Model()


