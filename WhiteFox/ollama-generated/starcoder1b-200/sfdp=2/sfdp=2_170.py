
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 4096)
        self.scale_factor = torch.nn.Parameter(torch.ones((1)))
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return output_projection(x2, v6)
 
    @property
    def scale_factor(self):
        return self._scale_factor
 

# Initializing the model
m = Model()


