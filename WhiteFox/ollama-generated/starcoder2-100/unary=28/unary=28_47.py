
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 512)
    
    def forward(self, x):
        v0 = torch.randn(32 * 8764).reshape(-1, 32, 512, 19)
        v1 = self.linear(v0[:, :, 128:512])
        v2 = torch.clamp_min(v1, min=x)
        v3 = torch.clamp_max(v2, max=y)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x  = -4 * np.ones((50, )) + 4
y  = x / 7
__output__  = m(x1)