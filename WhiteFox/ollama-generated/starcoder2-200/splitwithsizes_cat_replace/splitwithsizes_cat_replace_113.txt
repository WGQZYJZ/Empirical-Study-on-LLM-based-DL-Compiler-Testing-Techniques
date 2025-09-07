
class Model(torch.nn.Module):
    def __init__(self, split_dimension):
        super().__init__()
        self.split = torch.split
        self.concat = torch.cat
        self.split_dim  = split_dimension
 
    def forward(self, x1):
        v1 = self.split(x1, 32)
        v2 = [v1[i] for i in range(len(v1))] 
        v3 = self.concat(v2, dim=0)
        return v3


# Initializing the model
m  = Model(dim=self._split_dimension)


# Inputs to the model
x1  = torch.randn(967458, dtype=torch.float32).cuda()
__output__  = m(x1)