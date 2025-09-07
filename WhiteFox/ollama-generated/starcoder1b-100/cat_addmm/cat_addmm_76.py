
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, 1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.fc1.weight.t(), self.fc1.bias)
        return self.fc2(v1)


# Initializing the model
m = Model(3)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
