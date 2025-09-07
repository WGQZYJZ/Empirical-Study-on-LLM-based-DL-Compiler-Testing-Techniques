
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        with torch.random.fork_rng():
            # `torch.rand_like` or `lowmem_dropout` will be replaced by the corresponding functions. 
            v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()


