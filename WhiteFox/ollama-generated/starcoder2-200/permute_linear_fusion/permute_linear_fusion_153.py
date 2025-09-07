
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3 = x1.permute(0, 2, 1).transpose(-1, -2) # Permute the input tensor.
        v4  = self.linear(v3).clamp_min_(0.).exp()
        return torch.sum(v4 + self.linear.weight), torch.cat([v3[i] for i in range(len(v4))], dim=1)


# Initializing the model