
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v = torch.full([3], 2, dtype=torch.double, layout='cuda', device='cuda:0', pin_memory=False)
        return torch.cumsum(v)


# Initializing the model
m = Model()


