
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 1)
 
    def forward(self, x):
        v1  = self.linear(x)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(43, 256)

