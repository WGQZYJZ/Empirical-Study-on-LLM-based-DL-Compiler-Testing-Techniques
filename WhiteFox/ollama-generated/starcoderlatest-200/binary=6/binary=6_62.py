
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 8)
 
    def forward(self, x1, other):
        v1 = self.linear(x1.view(x1.shape[0], -1))
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
other  = torch.tensor([[1,1]]) # Other tensor that has been initialized by 'torch.randn'
x1     = torch.randn(100)
