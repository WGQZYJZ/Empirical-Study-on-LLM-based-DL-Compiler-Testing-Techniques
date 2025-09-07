
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1: torch.Tensor, inp2):
        v1 = torch.mm(inp1, inp2)  # Matrix multiplication operation on two input tensors
        v2 = v1 + inp
        return v2
 
m = Model()

