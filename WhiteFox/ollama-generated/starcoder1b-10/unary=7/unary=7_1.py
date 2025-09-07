
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8, bias=False)
        self.clamp    = torch.nn.ClampTensor()
 
    def forward(self, x1):
        l1 = self.linear1(x1)
        l2 = self.clamp(min=0, max=6, l1 + 3)
        l3 = l2 / 6
        return l3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
