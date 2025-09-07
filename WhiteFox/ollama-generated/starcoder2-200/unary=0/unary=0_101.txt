
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  *  0.5
        v3  = (v1 * v1).view(-1)[..., :].sqrt()[:, None]
        v4  = torch.diag_embed((v1 * v1 * v1).view(-1)[..., :]).sum(dim=2) / 9
        v6  = v3 + v4
        v7  = ((torch.tanh(v6) +  0.5088682911661262).float() * (v2 * torch.tensor([[-[ 0.4]]]) + (-v6).sum())).sum(dim=-3).sum().sum()
        return v7

# Initializing the model
m = Model()

