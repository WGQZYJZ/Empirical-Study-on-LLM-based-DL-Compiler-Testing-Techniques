
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 1)
 
    def forward(self, x1):
        return sigmoid(self.linear(x1))


# Initializing the model
m = Model()


