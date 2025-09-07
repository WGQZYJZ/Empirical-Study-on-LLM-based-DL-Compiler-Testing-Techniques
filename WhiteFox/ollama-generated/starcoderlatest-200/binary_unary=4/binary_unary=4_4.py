
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1, other=torch.tensor([0])):
        v1 = self.linear(x1) + other
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 32) # random input of shape (3, 32), data type is float
other = torch.tensor([0])
