
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, self.fc1(x2), self.fc2(x2))
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 64)
x2  = torch.randn(3, 64)
