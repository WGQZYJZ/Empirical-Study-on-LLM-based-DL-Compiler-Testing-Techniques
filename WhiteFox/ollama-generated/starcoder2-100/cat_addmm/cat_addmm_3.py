
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.concat = torch.nn.functional.softmax
        self.dim  = dim

    def forward(self, x1):
        v1 = torch.cat([x1], self.dim) # Concatenate the input along a specified dimension
