

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key  = torch.nn.Parameter(torch.randn([1024, 8]))
        self.value  = torch.nn.Parameter(torch.randn([3, 64, 5, 5], dtype=torch.float))
        self.query  = torch.nn.Parameter(torch.randn([3, 64, 1024, 1]))
 
    def forward(self):
        v1  = torch.matmul(self.key, self.value) / math.sqrt(v1.shape[-1]) * math.sqrt(self.query.shape[1])
        v2  = v1 + torch.randn([3, 64, 80], dtype=torch.float).div(math.sqrt(5))
        v3  = self._apply_dropout(v2) 
        v4  = torch.nn.functional.conv2d(self.query, self.key[None].permute([1, 0]).expand([-1] + list(self.query.shape))) * math.sqrt(5)
        return (v3, v4).mean()

m  = Model()
__output__  = m()

