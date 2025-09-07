
class Model(torch.nn.Module):
    def __init__(self, inp=123456):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1, bias=False)
        self.inp = inp
 
    def forward(self, x1):
        v1 = x1 * self.inp
        v2 = torch.mm(v1, x1.t()) + v1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2048) # (batch_size, num_features)
inp = torch.randn(4, self.inp)
