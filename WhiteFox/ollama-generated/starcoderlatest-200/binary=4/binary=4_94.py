
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 384)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other_tensor
        return v6


# Inputs to the model
x1 = torch.randn(1, 1024, 576, 32)
