
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 10, 5)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other # passing the "other" as a keyword argument to forward()
        v3 = torch.relu(v2) 
        return v3
# Initializing model with a custom tensor
other  = torch.zeros([5])
m  = Model()

