
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 16)
 
    def forward(self, x1, other=torch.tensor(5.5)):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = torch.nn.ReLU()(v2)
        return v3
# Inputs to the model
x1 = torch.randn(10, 20)
other = torch.tensor(3.5)
