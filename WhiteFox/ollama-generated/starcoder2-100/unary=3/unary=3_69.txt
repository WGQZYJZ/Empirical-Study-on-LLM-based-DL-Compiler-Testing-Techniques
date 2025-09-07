
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5 + 0.7071067811865476
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

## Questions:
- What is the minimum number of required API calls in `torch` to produce a valid PyTorch model?
- Do these rules always hold true?
- How can we make these rules more strict so that the produced model becomes much smaller and has less memory cost? 