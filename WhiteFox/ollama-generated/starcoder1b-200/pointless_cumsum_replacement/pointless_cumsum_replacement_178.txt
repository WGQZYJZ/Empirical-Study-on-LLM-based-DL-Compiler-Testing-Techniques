
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.full([x1.shape[0], 1], 1, device=device) * 2 + 1


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
