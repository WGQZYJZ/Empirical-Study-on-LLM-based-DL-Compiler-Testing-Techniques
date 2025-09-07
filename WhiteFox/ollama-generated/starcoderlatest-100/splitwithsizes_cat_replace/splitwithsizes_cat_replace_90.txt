
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = torch.split(x1, 3, dim=0)
        x3 = torch.cat([x for i in range(4)], dim=0) # Should trigger the is_valid_splitwithsizes_cat optimization.
        return x1


# Initializing the model
m = Model()

