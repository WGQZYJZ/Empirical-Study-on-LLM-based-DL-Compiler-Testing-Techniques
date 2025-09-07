
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1).view(-1, 64, 7 * 7)
        v2 = v1 - 5
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


