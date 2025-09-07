
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation 
        return v2


# Initializing model
m = Model()

# Input to the model
x1  = torch.randn(3, 8)
