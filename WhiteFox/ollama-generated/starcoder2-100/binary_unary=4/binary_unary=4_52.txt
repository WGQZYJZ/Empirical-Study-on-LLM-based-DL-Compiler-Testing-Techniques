
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = torch.relu(v1 + self.__other__)
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 64, 72)
__output__  = m(x1)
