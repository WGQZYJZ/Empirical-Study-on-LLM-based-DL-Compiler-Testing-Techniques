
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 10)

    def forward(self, x):
        l1 = self.linear(x)
        l2 = l1 * torch.clamp(min=0, max=6, input=(l1 + 3)) # Multiplication
        l3 = (l2 / 6).cuda()
        return l3


m = Model().cuda()

