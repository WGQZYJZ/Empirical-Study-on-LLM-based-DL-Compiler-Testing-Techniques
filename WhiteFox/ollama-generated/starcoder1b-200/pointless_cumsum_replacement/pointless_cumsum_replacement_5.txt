
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.full([arg1], 1, dtype=dtype, layout=layout, device=device)
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
