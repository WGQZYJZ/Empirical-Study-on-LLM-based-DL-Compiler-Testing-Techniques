
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(num_features=512)
 
    def forward(self, x1, x2, x3):
        v1 = x1 + x2 * (0.6 * x1)
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 * x3
        return self.layer_norm(v4)


# Initializing the model
m = Model()


