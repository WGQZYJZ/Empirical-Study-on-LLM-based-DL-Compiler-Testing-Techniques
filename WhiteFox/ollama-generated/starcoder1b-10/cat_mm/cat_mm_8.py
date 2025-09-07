
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.cat([x1 * x2], dim=-1)  # Here, `dim=-1` means concatenating along the last dimension (i.e., time).


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)  # Shape of input is `torch.Size([1, 3, 64, 64])`
x2 = torch.randn(4, 3, 64, 64)  # Shape of input is `torch.Size([1, 3, 64, 64])`
