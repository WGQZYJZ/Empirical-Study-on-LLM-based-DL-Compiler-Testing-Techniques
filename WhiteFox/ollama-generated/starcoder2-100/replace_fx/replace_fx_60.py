
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4096)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.25)
        v2 = torch.rand_like(v1) 
        v3 = self.linear1(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3)


