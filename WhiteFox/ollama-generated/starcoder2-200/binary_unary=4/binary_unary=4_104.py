
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        v0  = torch.nn.init.constant_(x1, -3) 
        v1  = self.linear(v0) + other
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model