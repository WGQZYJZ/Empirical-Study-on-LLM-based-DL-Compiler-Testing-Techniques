
class Model(torch.nn.Module):
    def __init__(self, max_value=2000):
        super().__init__()
        self.linear = torch.nn.Linear(512, 128)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -746339700)
        v3 = torch.clamp_max(v2, max_value=258)
        return v3


# Initializing the model with an additional argument
m  = Model()
__output__  = m(torch.randn(1, 512))