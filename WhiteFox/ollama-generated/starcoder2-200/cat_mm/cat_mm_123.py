
class Model(torch.nn.Module):
    def __init__(self, m1: int = 80) -> None:
        super().__init__()
        self._m1 = torch.nn.Linear(32, m1)
        self._m2 = torch.nn.Linear(m1 + 32, m1 // 4)
 
    def forward(self, x):
        v1 = F.relu(self._m1(x))
        v2 = F.relu(self._m2(torch.cat([v1, x], dim=0)))
        return torch.max(v1 + v2, 0)[0]

# Initializing the model
model = Model()

# Inputs to the model
x  = torch.rand(4, 32)
x1  = torch.randn(80)
__output___1__  = model([x]) # The forward call with inputs to the first module (containing the linear layer).
__output___2__  = model([torch.cat((v1[0].repeat(4,1), x), dim=0)]) # The forward call with inputs to the second module (containing the second linear layer).
__output___3__  = model([x]) # The forward call with inputs that are different from those of the previous modules.

