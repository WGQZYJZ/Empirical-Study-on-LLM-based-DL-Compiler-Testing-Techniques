
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1: torch.Tensor, inp2: torch.Tensor):
        t = torch.mm(inp1, inp2) + inp  # This call is not covered by the pattern
        return t


# Initializing the model
m  = Model()
 
# Inputs to the model
i1 = torch.randn([300, 5])
i2 = torch.randn([4, 300])
inp  = torch.tensor([[6] * 8]).repeat(7, 9)
