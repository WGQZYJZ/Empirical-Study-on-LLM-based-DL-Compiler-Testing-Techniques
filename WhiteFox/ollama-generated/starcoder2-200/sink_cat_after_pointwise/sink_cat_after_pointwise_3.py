
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.cat([v1, v3], dim=0)  # concatenation
        v3 = v2.view(-1, 64*3)           # reshape operation
        v4 = torch.relu(v3)               # pointwise unary operation: ReLU or Tanh

        return v4


# Initializing the model
m = Model()
__output__  = m(x1)

