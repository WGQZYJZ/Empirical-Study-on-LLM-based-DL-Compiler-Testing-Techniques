
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2dTranspose(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v2 * torch.tensor([0.044715])
        v4 = torch.tanh(v3)
        v5 = v1 + v4
        v6 = v5 * torch.tensor([0.7978845608028654])
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
