
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 4096)
        self.fc2 = torch.nn.Linear(4096, 4096)
 
    def forward(self, x1, x2, x3):
        v1 = F.elu(torch.nn.functional.linear(x1, self.fc1))
        v2 = F.elu(torch.nn.functional.linear(v1, self.fc2))
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32) # x1
x2 = torch.randn(4, 64) # x2
x3 = torch.randn(4, 64) # x3
