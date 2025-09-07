
class Model(torch.nn.Module):
    def __init__(self, inputsize=4096):
        super().__init__()

        self._input = torch.zeros(256 * 3, 128)
        self._linear = torch.nn.Linear(128 + inputsize, 768).to(self._input.device)

    def forward(self):
        x0 = self._input.clone().view(-1, 128, 4) # copy, reshape, and cast
        x1 = torch.cat([x0, torch.zeros_like(x0)], dim=-2).permute(0, 3, 1, 2).contiguous() # permute and concat, recast
        return self._linear(x1.view(-1, 514 + inputsize))

