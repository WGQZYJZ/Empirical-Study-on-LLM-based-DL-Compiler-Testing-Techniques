
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 200)
        self.linear2 = torch.nn.Linear(200, 32)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model