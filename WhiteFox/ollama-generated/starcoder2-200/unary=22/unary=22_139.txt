
class Model(torch.nn.Module):
    def __init__(self, dim1=32, dim2=64):
        super().__init__()
        self.linear = torch.nn.Linear(dim1, dim2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model