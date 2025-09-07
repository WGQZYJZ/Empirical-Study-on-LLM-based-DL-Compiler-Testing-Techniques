
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = (v1 ** 3)  + 1
        v4  = torch.tanh(v3) * 0.7978845608028654
        v5  = v2 + v4
        return v5
