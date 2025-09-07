
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.functional.linear

    def forward(self, x1, y2, z3, k4):
        a  = self.mm1(x1, y2)
        b  = self.mm1(z3, k4)
        c  = a + b
        return c


# Initializing the model