
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x1, v2):
        t1 = self.linear(x1)
        t2 = t1 + v2
        t3 = torch.nn.functional.relu(t2)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 8)
v2 = torch.randn(16)
