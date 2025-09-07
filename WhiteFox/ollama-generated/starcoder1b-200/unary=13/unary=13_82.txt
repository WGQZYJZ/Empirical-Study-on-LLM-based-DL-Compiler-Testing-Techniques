
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1).view(-1, 64 * 7 * 7)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()


