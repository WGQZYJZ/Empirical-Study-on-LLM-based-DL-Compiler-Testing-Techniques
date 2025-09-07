
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.dropout(x1) # Replaced by the fallback version in this example (lowmem_dropout).
        v4  = torch.rand_like(v3) # Replaced by the fallback version in this example (rand_like).
        return [v3, v4]

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(2, 50)
