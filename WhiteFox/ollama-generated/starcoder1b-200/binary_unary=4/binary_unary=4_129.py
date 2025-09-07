
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 20)
 
    def forward(self, x1, other=None):
        v1 = F.relu(self.linear(x1)) + other
        return v1


# Initializing the model
m = Model()

