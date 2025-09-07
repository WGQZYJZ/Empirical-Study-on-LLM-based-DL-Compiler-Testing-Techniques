
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.sig = torch.nn.Sigmoid()
 
    def forward(self, x1):
        return self.linear(x1) * self.sig(x1)


# Initializing the model
m = Model()

