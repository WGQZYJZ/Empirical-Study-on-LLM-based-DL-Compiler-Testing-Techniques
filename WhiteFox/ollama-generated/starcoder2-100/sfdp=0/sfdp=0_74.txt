
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, scale=None):
        super().__init__()
        self.scale = torch.tensor(float(scale), requires_grad=False)

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        # compute attention weights
        wq = q @ k.transpose(-2, -1) / self.scale 
        aw = torch.nn.functional.softmax(wq, dim=-1)
        # compute scaled dot product attetion
        ou = aw @ v

        return ou


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._sa_att = ScaledDotProductAttention()

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        out  = self._sa_att(q, k, v) 
        return out

m  = Model()

