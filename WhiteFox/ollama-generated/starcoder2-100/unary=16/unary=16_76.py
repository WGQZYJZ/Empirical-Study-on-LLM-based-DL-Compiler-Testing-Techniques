class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.relu(v1)
        return v2


m = Model()

# Inputs to the model
x1  = torch.randn(1, 320)
__output__  = m(x1)

