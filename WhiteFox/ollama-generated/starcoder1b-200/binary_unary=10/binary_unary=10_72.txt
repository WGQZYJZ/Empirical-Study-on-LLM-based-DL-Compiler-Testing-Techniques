
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 16)
 
    def forward(self, x):
        v1 = self.linear(x) + other
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


