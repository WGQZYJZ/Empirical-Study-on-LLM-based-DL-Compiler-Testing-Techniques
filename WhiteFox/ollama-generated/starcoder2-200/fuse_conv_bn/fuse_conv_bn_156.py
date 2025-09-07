
class ConvBN(torch.nn.Module):
    def __init__(self, inplanes: int = 32) -> None:
        super().__init__()
        
        # 1, 4, 9
        conv  = torch.nn.ConvNd(inplanes, 64, 5, stride=1, padding=0)
        bn   = torch.nn.BatchNormNd(conv.weight.shape[-1])

        self._bn   = bn
        self._conv = conv

    def forward(self, input: torch.Tensor):
        return torch.nn.functional.batch_norm(
            self._conv(input), 
            weight=self._bn.running_mean, bias=None)

m  = ConvBN()

