
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 256)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        l1 = self.linear1(x)
        l2 = l1 + 3
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 5) / 6
        return self.relu(self.linear2(l4))


# Initializing the model
m = Model()


