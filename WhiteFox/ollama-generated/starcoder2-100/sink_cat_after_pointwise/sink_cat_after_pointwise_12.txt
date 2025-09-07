
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:  # noqa: B906, E501
        v1 = torch.cat([x1, x2], dim=3) 
        v2 = v1.view(-1, 8 * 4)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
__x1_input__ = torch.randn(50, 7) # Dummy input for tensor x1 of shape (N, C).
__x2_input__ = torch.randn(48, 7, 9) # Dummy input for tensor x2 of shape (N, C, D). 

# Initializing the model output with an arbitrary value.
__output___  = m(__x1_input__, __x2_input__)

