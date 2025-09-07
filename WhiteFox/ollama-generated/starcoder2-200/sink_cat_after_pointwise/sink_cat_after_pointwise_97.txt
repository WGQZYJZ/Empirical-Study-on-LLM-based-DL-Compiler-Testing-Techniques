
class Model(torch.nn.Module):
    def __init__(self, num1):
        super().__init__()
        self.linear  = torch.nn.Linear(num1 + 1, 2)

    def forward(self, x1):
        v3 = torch.cat([x1, torch.tensor(0.).cuda(), torch.tensor([5., 6., ])], dim=2)
        v4 = self.linear(v3.view(-1, num1 + 1))
        return v4


# Initializing the model
m = Model()

# Inputs to the model
__input1__ = torch.randn(5, 6, device='cuda')

