

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other # ADD_START
        v3  = v2 * 0.5
        return v3

# Initializing the model
m = Model()

