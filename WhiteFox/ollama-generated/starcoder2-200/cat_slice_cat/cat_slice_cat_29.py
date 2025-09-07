
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 3)
        self.linear2 = torch.nn.Linear(9, 4)
 
    def forward(self, x):
        v1 = self.linear1(x[:, :9])
        v2 = self.linear2(v1[:,:7])
        v3 = self.linear2(v1[0:size,:])
 
        return torch.cat([v2, v3], 0)


# Initializing the model
m = Model()
# Inputs to the model
__output__  = m(torch.randn(1, 9))

