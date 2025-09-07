
class Model(torch.nn.Module):
    def __init__(self, hidden_size=128):
        super().__init__()
        self.linear = torch.nn.Linear(1024, hidden_size)
 
    def forward(self, x):
        v1 = self.linear(x) + 1
        return v1


# Initializing the model
m = Model()


