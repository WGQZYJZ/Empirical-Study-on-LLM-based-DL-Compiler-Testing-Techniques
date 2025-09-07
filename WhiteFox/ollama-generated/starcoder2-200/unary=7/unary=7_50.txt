
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.l1 = torch.nn.Linear(5, 3072)

    def forward(self, x1): 
        l1 = self.l1(x1)
        l2 = l1 * torch.clamp(min=0, max=6, input=l1 + 3.) / 6.
 
        return l2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5)
