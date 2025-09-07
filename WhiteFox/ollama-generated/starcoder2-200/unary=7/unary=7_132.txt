
class Model(torch.nn.Module):
    def __init__(self, f=0., l=1.) -> None:
        super().__init__()

        self.layer = torch.nn.Linear(32 * 32 * 8, 64)
 
        self.f = f
        self.l = l

    def forward(self, x):
        v = self.layer(x).reshape(-1, 8, 32, 32)
        
        # Apply SELU activation
        y = torch.where((v > 0), v * self.f + self.l,
                         (v + torch.sign(v)) * self.f / 2.)

        return y
