
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
        self.linear2 = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        v1 = self.linear1(x) 
        v2 = v1 * nn.functional.relu6(v1 + 3) 
        v3 = v2 / 6
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(4, 64)


__output__  = m(x)
