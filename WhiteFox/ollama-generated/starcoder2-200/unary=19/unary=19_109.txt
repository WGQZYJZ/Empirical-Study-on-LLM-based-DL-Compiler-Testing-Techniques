
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*84*70, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1)

        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 256*84*70) # random input of size (64, 3920640)


