
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 1)
 
    def forward(self, x1): 
        l1  = self.linear(x1).view(-1)
        l2 = (l1 + 3).clamp(min=0).clamp(max=6) / 6
        return l2

# Initializing the model