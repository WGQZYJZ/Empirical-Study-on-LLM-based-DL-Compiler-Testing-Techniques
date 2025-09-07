
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 480, dim=3)
        c1 = torch.cat([s1[i] for i in range(len(s1))], dim=3)
        return c1


# Optimized model after the `is_valid_splitwithsizes_cat` optimization is applied
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 480, dim=3)
        c1 = torch.cat(s1, dim=3)
        return c1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
