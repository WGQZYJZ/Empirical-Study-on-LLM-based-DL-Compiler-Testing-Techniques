
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model and feeding an input to it
m = Model()
x1 = torch.randn(48, 20)
