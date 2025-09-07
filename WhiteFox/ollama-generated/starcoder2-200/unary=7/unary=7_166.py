
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(4, 3)
 
    def forward(self, x1):
        y1 = self.linear(x1)

        y2 = y1 * torch.clamp(min=0, max=6, input=y1 + 3).div(6.)
        return y2


m_2 = Model2()
