
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v6

# Input to the model
other = torch.randn(3, dtype=torch.float64, requires_grad=True)
__output__  = m(x1)

