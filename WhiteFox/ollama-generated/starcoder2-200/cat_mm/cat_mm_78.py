
class Model(torch.nn.Module):
    def __init__(self, m1: torch.Tensor, m2: torch.Tensor) -> None:
        super().__init__()
        self.m1  = m1
        self.m2  = m2
 
    def forward(self, v):
        v1  = torch.mm(v, self.m1)
        v2  = torch.cat([v1, v1], dim=0)
        return v2


m_m1  = torch.randn(43, 798)
m_m2  = torch.randn(43, 556)
__input1__, __input2__, 