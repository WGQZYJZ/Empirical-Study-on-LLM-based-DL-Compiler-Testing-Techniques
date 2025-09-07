
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear  = torch.nn.Linear(3072, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0
        v3  = -v1 * 0.5 + 1
        v4  = torch.where(v2, v1, v3) # Where v2 is true (greater than zero), set v1 to itself; where it's false (not greater than 0), set it equal to the negative half of itself plus one.
        return v4

# Initializing the model
m = Model()

