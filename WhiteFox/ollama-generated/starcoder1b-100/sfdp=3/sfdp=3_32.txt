
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 32)
        self.linear2 = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = F.relu(self.linear1(x1))
        v2 = self.linear2(v1)
        return v2


# Initializing the model
m = Model()


