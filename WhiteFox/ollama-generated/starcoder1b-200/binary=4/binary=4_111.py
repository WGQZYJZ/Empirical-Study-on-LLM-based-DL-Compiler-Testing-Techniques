
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 10)
 
    def forward(self, x):
        y  = self.linear(x) + other
        return y


# Initializing the model
m = Model()
