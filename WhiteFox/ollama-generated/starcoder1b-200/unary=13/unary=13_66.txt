
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        return self.sigmoid(self.linear(x1))


# Initializing the model
m = Model()


