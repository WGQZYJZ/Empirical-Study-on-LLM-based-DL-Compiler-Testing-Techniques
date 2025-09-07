
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, xs): 
        return torch.cat([xs[0], xs[-1][-9223372036854775807:]], 0)


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = [torch.randn(1, 5), torch.randn(1, 5)]
