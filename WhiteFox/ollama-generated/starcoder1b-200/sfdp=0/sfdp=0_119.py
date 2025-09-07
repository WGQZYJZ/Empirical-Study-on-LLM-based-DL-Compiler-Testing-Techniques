
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.DotProduct()
        self.scale = torch.sqrt(torch.ones((3, 4)))
 
    def forward(self, x1, x2):
        v1 = self.scaled_dot_product(x1, x2) / self.scale
        return v1

# Initializing the model
m = Model()


