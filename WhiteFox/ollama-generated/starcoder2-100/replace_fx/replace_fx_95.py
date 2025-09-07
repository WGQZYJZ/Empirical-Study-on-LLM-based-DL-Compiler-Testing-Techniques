
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # replace torch.rand_like with rand_like
        v1 = torch.rand_like(x1)
        v2 = torch.nn.functional.dropout(v1, ...) 
        return v2

# Initializing the model
m = Model()


# Inputs to the model