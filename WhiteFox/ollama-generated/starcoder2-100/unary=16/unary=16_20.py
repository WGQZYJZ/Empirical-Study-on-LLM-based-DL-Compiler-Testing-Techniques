
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = nn.functional.relu(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3072,)
