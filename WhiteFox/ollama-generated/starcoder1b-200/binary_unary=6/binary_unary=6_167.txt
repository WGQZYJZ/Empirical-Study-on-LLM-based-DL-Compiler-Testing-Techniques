
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return relu(v1 - other)


# Initializing the model
m = Model()
