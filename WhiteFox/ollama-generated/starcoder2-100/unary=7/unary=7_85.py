
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 128, bias=False)
 
    def forward(self, x1):
        l1  = self.linear(x1)
        l2  = l1 * clamp(min=0, max=6, l1 + 3) # line 9
        l3  = l2 / 6 # line 7
        return l3

# Initializing the model