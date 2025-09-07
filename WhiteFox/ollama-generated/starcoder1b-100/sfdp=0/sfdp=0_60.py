
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2):
        v1 = self.scaled_dot_product(x1)
        v2 = self.scaled_dot_product(x2)
        return (v2 / inv_scale) * (v1 + bias)


# Initializing the model
m = Model()


