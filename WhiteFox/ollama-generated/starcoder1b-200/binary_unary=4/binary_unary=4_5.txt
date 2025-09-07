
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(100, 50)
 
    def forward(self, x):
        v = self.linear(x) + other
        return relu(v)


# Initializing the model
m = Model()


