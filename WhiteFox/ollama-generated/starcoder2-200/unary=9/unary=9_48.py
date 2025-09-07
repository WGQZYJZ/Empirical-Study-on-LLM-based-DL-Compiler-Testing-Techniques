

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1  = self.conv2d1(x)
        v2a = torch.ones_like(v1) * 3
        v4  = v1 + v2b
        v5c = torch.clamp_min(v4, 0)
        v6e = torch.clamp_max(v5c, 6)
        v7f = v6e / 6
        return v7g
 

# Initializing the model<|end_of_model|>

model  = Model()


# Inputs to the model<|end_of_input|>

