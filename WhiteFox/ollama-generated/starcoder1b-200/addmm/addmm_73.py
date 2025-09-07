
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1: torch.Tensor = None):
        if x1 is None:
            inp = self.inp # No input provided; just use the value of 'inp' as the input to the model
        else:
            inp = x1 # Use the input argument provided by PyTorch APIs

        ...
        return out


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
