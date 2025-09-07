
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1: torch.Tensor, inp2: torch.Tensor, inp3: torch.Tensor = None) -> torch.Tensor:
        v1  = torch.mm(inp1, inp2) # The matrix multiplication operation takes place on the two input tensors
        v2  = v1 + inp3 
        return v2


# Initializing the model with keyword argument
m = Model()


# Inputs to the model
x1  = torch.randn(500, 784) # 500 training samples with 784 dimensions each
x2  = torch.randn(784, 60) # 784 input features for each of these 500 training samples 

x3  = None if m.inp3 is not required else torch.randn(100)

