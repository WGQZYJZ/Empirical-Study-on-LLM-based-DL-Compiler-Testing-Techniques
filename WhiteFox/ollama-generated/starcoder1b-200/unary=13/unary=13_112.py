
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128 * 4 * 4, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 128, 4, 4))
        return v3


# Initializing the model
m = Model()
