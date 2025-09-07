
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if not isinstance(other, (float, int)):
            other = torch.from_numpy(np.array(other))
        v2 = v1 + other
        return v3

# Initializing the model
m  = Model()


