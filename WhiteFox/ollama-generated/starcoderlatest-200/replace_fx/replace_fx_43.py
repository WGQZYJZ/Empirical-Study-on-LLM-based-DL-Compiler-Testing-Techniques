 
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5, inplace=False)
        t2 = torch.rand_like(x1)
        return torch.cat((t1, t2), dim=1)
# Initializing the model 
m2 = Model()


# Inputs to the model
x2 = torch.randn(3, 2, 4)
