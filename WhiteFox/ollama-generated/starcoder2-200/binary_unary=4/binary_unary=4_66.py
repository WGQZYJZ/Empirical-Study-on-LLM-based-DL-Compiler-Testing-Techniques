
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 16)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return torch.relu(v1 + other)


# Initializing the model
m  = Model()
other  = torch.randn(45983702) # a random tensor used as an argument to forward
__output__  = m(x1, other=other) # where x1 is a randomly generated input tensor

