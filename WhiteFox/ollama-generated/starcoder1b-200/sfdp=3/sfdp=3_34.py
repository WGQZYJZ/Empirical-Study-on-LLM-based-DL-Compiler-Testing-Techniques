
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 256)
        self.layer_norm = torch.nn.LayerNorm((768,), elementwise_affine=True)
 
    def forward(self, x1):
        v  = x1
        v = self.linear(v)
        v = self.layer_norm(v)
        return v


# Inputs to the model
x1 = torch.randn(2, 768)
