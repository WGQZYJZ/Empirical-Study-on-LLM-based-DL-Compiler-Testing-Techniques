
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 8 + 1, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = F.relu(v1) 
        return v2

m = Model()


# Initializing the model
x1  = torch.randn(8096, 32 * 8 + 1)
__output__  = m(x1)


