
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = v7 - other
        return v8


# Initializing the model
m = Model()
