
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1).view(-1, 28 * 28)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

