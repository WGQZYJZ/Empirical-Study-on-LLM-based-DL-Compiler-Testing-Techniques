
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16, bias=False)
 
    def forward(self, x2):
        l1 = self.linear(x2)
        l2 = l1 * clamp(min=0, max=6, l1 + 3)
        l3 = l2 / 6
        return l3
# Initializing the model
m = Model()

 # Inputs to the model
 x2 = torch.randn(1, 3, 64, 64)
 