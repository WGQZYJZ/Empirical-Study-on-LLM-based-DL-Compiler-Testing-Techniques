
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 ** 2, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = F.relu(v1) # This line is the difference from Model above!
        return v2


# Initializing the model and applying it to inputs