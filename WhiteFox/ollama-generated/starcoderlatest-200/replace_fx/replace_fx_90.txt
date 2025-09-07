
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.2)
        v2 = torch.rand_like(v1, dtype=torch.float64)
        return self.linear(v2).sum()


# Initializing the model
m = Model()
gm = GM(m, [x1])
gm.randomize("lowmem_dropout") # or gm.randomize("rand_like")
