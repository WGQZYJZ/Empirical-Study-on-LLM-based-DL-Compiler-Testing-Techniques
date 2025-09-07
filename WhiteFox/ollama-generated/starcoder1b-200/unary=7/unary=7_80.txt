
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 16, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        clamped_v2 = min(max(v1 + 3, 0), 6) / 6
        scaled_v3 = clamped_v2 * torch.expm1(-clamped_v2)
        return v3


# Initializing the model
m = Model()


