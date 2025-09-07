
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v2  = torch.nn.functional.adaptive_avg_pool2d(x1, output_size=(3, 5))
       v3  = v2 * 0.7071067811865476
       v4  = torch.erf(v3)
       v5  = v4 + 1
       return v5

# Initializing the model
m  = Model()

 # Inputs to the model