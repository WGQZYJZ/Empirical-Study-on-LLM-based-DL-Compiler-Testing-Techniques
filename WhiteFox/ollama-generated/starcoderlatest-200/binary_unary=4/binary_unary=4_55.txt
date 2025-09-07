
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.relu = torch.nn.ReLU()
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + (self.other if self.other is not None else x1)
        v3 = self.relu(v2)
        return v3


# Initializing the model and passing the `other` tensor as a keyword argument to the forward method
m = Model()
x1 = torch.randn(1, 3, 64, 64)
