
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(2048, other)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 5.3
        return v1


# Initializing the model
m = Model(2)

