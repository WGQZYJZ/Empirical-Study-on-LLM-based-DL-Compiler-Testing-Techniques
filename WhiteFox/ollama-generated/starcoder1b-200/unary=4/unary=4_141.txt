
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v = self.linear(x)
        return v * 0.5 + v * 0.7071067811865476


# Initializing the model
m = Model()


