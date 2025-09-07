
class Model(torch.nn.Module):
    def __init__(self, m=None):
        super().__init__()
        if m:
            self.m = m
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, 0 for _ in range(len(x1))]) # The number of repetitions for each element should be the same as its dimension in tensor 1
        return self.m(v2)
# Initializing the model
m = Model()


