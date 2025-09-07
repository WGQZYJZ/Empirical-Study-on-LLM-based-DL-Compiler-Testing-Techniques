
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 8192)
 
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = v1 * clamp(min=0, max=6, l1 + 3) # min = 0, max = 6 and l1 + 3 = 3.4, so l1 should be set to -3 for the first part of clamp
        v3 = v2 / 6 
        return v3


# Initializing the model