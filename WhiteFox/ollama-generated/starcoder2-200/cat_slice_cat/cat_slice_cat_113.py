
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.cat([x1[:, :9223372036854775807],
                          x1[:, 9223372036854775807:]], dim=1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2*int(math.sqrt(1e9)), 64, 64)

