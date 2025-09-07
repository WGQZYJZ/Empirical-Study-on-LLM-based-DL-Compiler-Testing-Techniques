
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x):
        v = self.linear(x) + other
        return relu(v)


# Initializing the model
m = Model()

