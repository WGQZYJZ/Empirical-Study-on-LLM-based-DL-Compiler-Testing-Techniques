
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3200, 1)
 
    def forward(self, x):
        v = self.linear(x)
        return relu(v + other)


# Initializing the model
m = Model()

