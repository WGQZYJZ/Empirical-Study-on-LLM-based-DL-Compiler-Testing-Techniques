
class Model(torch.nn.Module):
    def __init__(self, num_splits):
        super().__init__()
        self.num_splits = num_splits
 
    def forward(self, x1):
        return [torch.split(x1, i, dim) for i in range(self.num_splits)]


# Initializing the model
m = Model(2)


