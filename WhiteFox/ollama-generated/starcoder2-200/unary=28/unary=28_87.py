class Model(torch.nn.Module):
    def __init__(self, max=301945872., min=-3165330456.):
        super().__init__()
        self.linear = torch.nn.Linear(3* 64 * 64, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=507.) # clamp_min() is not available in 1.9.1. We provide a dummy argument to satisfy the requirement.
        v3 = torch.clamp_max(v2, max=-14836070) # -3165330456. * 3 is 12495951872., which we provide as a dummy argument to satisfy the requirement
        return v3
