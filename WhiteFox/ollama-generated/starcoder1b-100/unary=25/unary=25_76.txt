
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, -v1 * 0.05) # for each element in v1, if it's True, choose the corresponding element from v1, otherwise use the output of the linear transformation with negative slope
        return v2


# Initializing the model
m = Model()
