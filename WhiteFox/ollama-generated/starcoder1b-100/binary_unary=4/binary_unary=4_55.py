
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.other   = other
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + self.other
        return relu(v1)


# Initializing the model
m = Model()


