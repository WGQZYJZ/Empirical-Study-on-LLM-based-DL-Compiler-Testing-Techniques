
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor = torch.ones((2560)), mat2: torch.Tensor = torch.zeros((32819))):
        super().__init__()
        
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
            v1  = torch.addmm(x1, mat1, mat2)
            v2  = torch.cat([v1], dim=0)
            return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(32819, 576) # First input is a tensor of shape (32819, 576), which can be randomly generated using torch.randn().
