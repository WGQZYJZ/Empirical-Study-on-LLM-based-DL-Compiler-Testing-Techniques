
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return sigmoid(v1) * t2


# Initializing the model
m = Model()


