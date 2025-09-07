
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1).view(-1, 64)
        return v1


# Initializing the model
m = Model()


