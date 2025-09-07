

class ScaledDotProductAttention(torch.nn.Module):

    def __init__(self, inv_scale):
        super().__init__()

        self.inv_scale = torch.nn.Parameter(
            data=torch.tensor([1 / math.sqrt(2048)]), requires_grad=False)

        self._register_parameter('inv_scale', self.inv_scale)

    def forward(self, query, key):
        