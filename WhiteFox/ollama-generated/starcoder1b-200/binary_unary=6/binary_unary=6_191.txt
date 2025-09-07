
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return (v1 - 0.5).relu()


# Initializing the model
m = Model()

