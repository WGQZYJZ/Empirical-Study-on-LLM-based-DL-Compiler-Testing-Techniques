
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Inputs to the model
x1 = torch.randn(16, 8) # (B, H_out) with random values sampled from standard normal distribution
x2 = torch.randn(16, 4) # (B, H_in) with random values sampled from standard normal distribution
