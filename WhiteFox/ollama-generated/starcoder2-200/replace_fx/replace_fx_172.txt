
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.25) # dropout
        v2 = torch.rand_like(v1) # rand_like
        return v1 + v2

# Initializing the model
m  = Model()

