
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_sizes = [8, 16]
 
    def forward(self, x):
        v1 = torch.split(x, self.split_sizes, dim=0)
        v2 = torch.cat([v1[i] for i in range(len(self.split_sizes))], dim=0)
        return v2


# Initializing the model
m = Model()


