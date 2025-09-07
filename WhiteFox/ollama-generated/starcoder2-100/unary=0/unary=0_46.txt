
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3 * 0.044715
        v6 = torch.tanh((v1 + v3).abs() / (torch.sqrt(torch.expm1(-v1**2)))) * torch.nn.Softplus()
        return v2 + v6
