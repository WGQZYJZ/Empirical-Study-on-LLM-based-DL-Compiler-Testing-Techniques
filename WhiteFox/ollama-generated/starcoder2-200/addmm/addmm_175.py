
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1: torch.Tensor, inp2 : torch.Tensor) -> torch.Tensor:
        v1 = torch.mm(inp1, inp2) #Perform matrix multiplication on two input tensors
        v2  = v1 + inp
        return v2


# Initializing the model
m = Model()
