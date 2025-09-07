
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784,10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2  = nn.functional.clamp_min(v1, min= -9375) # Clamp the minimum value to -9375
        v3 = nn.functional.clamp_max(v2, max=-9068) # Clamp the maximum value to -9068
        return v3

# Initializing the model
m  = Model()

