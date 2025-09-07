
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight)
        return v1

 # Initializing the model
  m  = Model()

# Inputs to the model
x2  = torch.randn(30, 50).cuda()
__output__  = m(x2)