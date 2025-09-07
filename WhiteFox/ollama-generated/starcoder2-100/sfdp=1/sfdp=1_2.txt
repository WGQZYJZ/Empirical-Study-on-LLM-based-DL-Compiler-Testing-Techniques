
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale  = torch.nn.Parameter(torch.rand((32, )))
        self.inv_scale  = (
            self.scale.masked_fill_(
                self.scale < 0.,
                1e-5) ** -1).unsqueeze(-1).unsqueeze(-1).unsqueeze(-1)
 
        self.query = torch.nn.Parameter(torch.rand((32, 32)))
        self.key  = torch.nn.Parameter(torch.rand((32, 32)))
        self.value  = torch.nn.Parameter(torch.rand((8, 32)))
 
    def forward(self):
        v1 = torch.matmul(self.query, self.key.transpose(-2, -1))
 
        v2 = v1 / self.inv_scale[None] * (
            self.inv_scale ** .5).masked_fill_(v1 < 0., 1e-7)
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.99)
 
        v6  = (
            torch.matmul(
                self._cast_float_(
                    v4), 
                    self.value).div(
                    self.scale.masked_fill_(
                        self.scale < 1e-5,
                        1)) ** -2).masked_fill_(v3 == 0., float('inf')) ** .5
        )
 
        v7 = torch.nn.functional.dropout(
            (
                torch.rand((48))
                ).abs().softmax(), p=0.99)

        return ((
            6 * v1).div(self._cast_float_(v3).sum(-2)).matmul(v4))
