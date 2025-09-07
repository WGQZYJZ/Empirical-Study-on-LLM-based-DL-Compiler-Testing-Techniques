
class Model(torch.nn.Module):
    def __init__(self, other=10):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 10
        return v1


# Initializing the model
m = Model()


