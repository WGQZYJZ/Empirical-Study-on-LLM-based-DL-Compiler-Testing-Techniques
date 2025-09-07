
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 3)
 
    def forward(self, x1):
        v1 = torch.relu(self.linear(x1))
        return v1


# Initializing the model
m = Model()


