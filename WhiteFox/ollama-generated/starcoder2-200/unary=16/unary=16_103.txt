
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(320 * 5, 4)
 
    def forward(self, x1):
        v1 = F.max_pool2d(x1[:, :320], 8, stride=None, padding=[1] * len(x1))
        v2 = torch.relu(v1)
        return self.lin(v2.view(-1, 320 * 5))


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(49768, 1)
__output__  = m(x1)

