
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(5, 8)
        self.relu1 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - other
        v3 = self.relu1(v2)
        return v3


# Initializing the model
m  = Model2()


# Inputs to the model
