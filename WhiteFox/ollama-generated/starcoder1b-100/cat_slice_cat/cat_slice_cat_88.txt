
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.cat([x1[:, 0:size], x2[:, 0:size]], dim=1)


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 10)
