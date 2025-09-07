
class LinearNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 40)
        self.linear2 = torch.nn.Linear(40, 28)
 
    def forward(self, x):
        v1  = self.linear1(x)
        v2  = self.linear2(v1) + x
        return v2


# Inputs to the model
input_tensor = torch.randn(3, 64, 64)
other       = torch.randn(3, 64, 64)
__output__  = LinearNet()(input_tensor, other)

