
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).type_as(x1) * (-v1 + 1)
        v3 = ((-v1 + 1).type_as(x1)).tanh()
        return v4


# Initializing the model
m = Model()


