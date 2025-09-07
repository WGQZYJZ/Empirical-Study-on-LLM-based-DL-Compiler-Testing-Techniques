
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.randn(30)
        v5  = x1 * -4
        v6  = x1 + v2
        v7  = torch.norm(v6, p=2, dim=-1) ** -1 / inv_scale
        v8  = torch.matmul(v5, torch.t(v7))  # Scaled dot product attention
        return v8


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(30) 
