
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...) # This line triggers replace_fx optimization
        v2 = torch.rand_like(...) # This line triggers replace_fx optimization
        return v2


# Running the script with fallback_random on CPU device
m = Model()
gm.set_fallback_random(True)
