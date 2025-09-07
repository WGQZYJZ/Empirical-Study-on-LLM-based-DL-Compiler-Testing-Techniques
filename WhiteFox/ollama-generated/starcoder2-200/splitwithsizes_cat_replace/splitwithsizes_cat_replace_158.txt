
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split  = torch.split(torch.rand(4,1024), (103,), dim=1)
        self.concat = torch.cat([self.split[i] for i in range(len(self.split))], 1)
 
    def forward(self):
        return __output__


m = Model()
 
# Inputs to the model
x = m()
 
