
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.3)
        v2 = torch.rand_like(v1)
        return v2


# Initializing the model and generating a random seed for replacing operations with fallback ones
m = Model()
m.random_seed = '46'
