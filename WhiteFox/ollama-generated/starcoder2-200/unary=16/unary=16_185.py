
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320 * 4, 1)
 
    def forward(self, x):
        return torch.relu(self.linear(x))
 
# Initializing the model
m = Model()


