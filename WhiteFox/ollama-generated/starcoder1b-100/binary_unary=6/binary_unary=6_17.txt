
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 2
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

