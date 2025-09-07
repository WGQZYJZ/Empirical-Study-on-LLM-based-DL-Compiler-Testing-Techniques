
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._a = torch.tensor([2,3], dtype=float)
 
    def forward(self, inp1: Tensor):  # Use positional argument
        v1 = torch.mm(inp1, torch.ones_like(inp1))
        return v1 + 6
 
m = Model()

