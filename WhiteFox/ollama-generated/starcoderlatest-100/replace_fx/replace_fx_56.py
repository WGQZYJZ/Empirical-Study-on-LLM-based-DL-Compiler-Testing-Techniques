
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x):
        t1 = torch.nn.functional.dropout(x, p=0.5, training=True) # replace_fx
        t2 = torch.rand_like(t1, dtype=torch.float)                # fallback_random
        self.linear(t2)
        return t1

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 3, 5)
