
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Method 1: Use torch.rand_like to replace torch.nn.functional.dropout
        t1 = torch.rand_like(x1)

        return t1

# Initializing the model
m  = Model()

# Inputs for the model
x1 = torch.ones(4, 4)
