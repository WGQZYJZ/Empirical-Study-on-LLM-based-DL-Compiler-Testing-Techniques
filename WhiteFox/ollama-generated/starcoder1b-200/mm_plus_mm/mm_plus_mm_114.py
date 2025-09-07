
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(64, 32)
 
    def forward(self, x):
        h = self.linear1(x)
        m = self.linear2(h)
        return m


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(64, 3, 8)
input2 = torch.randn(32, 8, 8)
