
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4096, bias=False)
 
    def forward(self, x1):
        l2  = torch.clamp(min=0, max=6, input=(x1 + 3))
        l3 = l2 / 6 
        return l3


# Initializing the model