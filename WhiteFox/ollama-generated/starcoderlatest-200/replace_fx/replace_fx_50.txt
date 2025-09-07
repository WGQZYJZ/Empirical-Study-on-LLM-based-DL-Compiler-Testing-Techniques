
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(p=0.5, inplace=True)

    def forward(self, x1):
        v1  = torch.rand_like(x1)
        v2 = self.dropout(x1) # this line will be erased if fallback_random is False and gm.platform == 'cpu'
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 5)
