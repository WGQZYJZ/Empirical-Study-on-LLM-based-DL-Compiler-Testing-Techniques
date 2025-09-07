
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 1)
 
    def forward(self, x1):
        x2 = torch.relu(x1.view(x1.shape[0], -1))
        x3 = self.linear(x2)
        return x3


# Initializing the model
m = Model()

