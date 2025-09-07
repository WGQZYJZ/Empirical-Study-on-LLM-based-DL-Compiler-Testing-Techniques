
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 50)
        self.linear2 = torch.nn.Linear(50, 300)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2 = v1 - other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()

# Input to the model