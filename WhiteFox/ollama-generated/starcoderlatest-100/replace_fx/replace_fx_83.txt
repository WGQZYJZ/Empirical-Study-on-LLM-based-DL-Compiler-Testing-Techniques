
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, inplace=True)
        v2 = torch.rand_like(v1)
        return v2

# Initializing the model and applying replacements for all random ops in the graph
m = Model()
gm.replace_fx()


# Inputs to the model 
x1 = torch.randn(1, 2, 2)
