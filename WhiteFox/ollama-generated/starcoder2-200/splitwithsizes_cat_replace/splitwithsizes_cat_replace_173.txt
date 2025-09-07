
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.split(x1)
        return torch.split(v1, [5], dim=-1)


# Initializing the model
m = Model()

# Inputs to the model 
x1  = torch.randn(8, 3, 64, 64)
__output__  = m(x1)

__expected_output__  = [(v2, 0), (v2, 1)]

