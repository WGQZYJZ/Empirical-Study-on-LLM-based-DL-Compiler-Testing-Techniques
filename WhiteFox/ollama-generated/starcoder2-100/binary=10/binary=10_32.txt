
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 1)
 
    def forward(self, x):
        v2 = self.linear(x) + other 
        return v2
 
# Initializing the model
m  = Model()

