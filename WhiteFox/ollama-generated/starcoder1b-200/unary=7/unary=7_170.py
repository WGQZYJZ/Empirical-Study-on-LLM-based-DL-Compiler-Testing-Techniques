
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8, bias=True)
 
    def forward(self, x1):
        l1 = self.linear1(x1)
        l2 = l1 * clamp(min=0, max=6, l1 + 3) / 6
        return l2


# Initializing the model
m = Model()

