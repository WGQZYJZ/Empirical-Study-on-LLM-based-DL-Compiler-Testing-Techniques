
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 10)
 
    def forward(self, x):
        return self.linear1(x) + self.linear2(torch.relu(self.linear1(x)))

# Initializing the model
m = Model()

