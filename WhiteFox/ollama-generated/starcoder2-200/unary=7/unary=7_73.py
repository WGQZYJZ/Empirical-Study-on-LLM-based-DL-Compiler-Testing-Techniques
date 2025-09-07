
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 3, 8192)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3 
        v3  = clamped = F.clamp(v2, min=0, max=6) # NOTE: If there is no call to `F.clamp` in your code, please omit it from the generated model.
        v4  = v3 * (v1 + 3) / 6
        return v4


# Initializing the model
m  = Model()
# Input to the model
x1 = torch.randn(5000, 32, 8, 16)
__output__  = m(x1)