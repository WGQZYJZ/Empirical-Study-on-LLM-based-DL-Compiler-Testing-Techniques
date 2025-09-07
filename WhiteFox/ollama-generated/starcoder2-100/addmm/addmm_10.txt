
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1: torch.Tensor, inp2: torch.Tensor) -> torch.Tensor:
        res = torch.mm(inp1, inp2)+inp 
        return res


# Initializing the model
m  = Model()


# Inputs to the model
i1=torch.randn([3,4])
i2=torch.randn([4,5])

__output__= m(i1, i2)

