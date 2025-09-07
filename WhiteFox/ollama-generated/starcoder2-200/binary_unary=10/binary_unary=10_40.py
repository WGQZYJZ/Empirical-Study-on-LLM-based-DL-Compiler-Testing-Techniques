
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024 * 3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other # Here `other` is a tensor obtained by another API call (you have to pass `m` into this API and then you can use it)
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m, other  = Model(), torch.randn(1024 * 3).cuda()

# Inputs to the model
x1  = torch.randn(8, 512, 3).cuda()
__output__  = m(x1)

