
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, x):
        v1 = self.linear(x) - 0.5
        return relu(v1)


# Initializing the model
m = Model()

