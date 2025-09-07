
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 5)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        return v1 + kwargs["other"]


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
