
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 16)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - 0.5
        v3 = relu(v2)
        return v3


# Initializing the model
m = Model()


