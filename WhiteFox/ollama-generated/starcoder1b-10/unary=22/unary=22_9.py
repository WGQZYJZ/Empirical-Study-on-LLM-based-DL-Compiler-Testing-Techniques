
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 8, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.tanh(v1)


# Initializing the model
m = Model()


