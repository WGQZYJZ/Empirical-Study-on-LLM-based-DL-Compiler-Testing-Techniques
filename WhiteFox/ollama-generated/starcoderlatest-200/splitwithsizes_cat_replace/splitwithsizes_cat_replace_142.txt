
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v  = torch.split(x1, 32, dim=1)
        concat_v = torch.cat(v, dim=1)
        return concat_v

# Inputs to the model
input_tensor = torch.randn(4096, 3, 64, 64)
