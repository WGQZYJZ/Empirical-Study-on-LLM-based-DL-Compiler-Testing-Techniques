
class Model(torch.nn.Module):
    def __init__(self, qk_channels):
        super().__init__()
        self.query = torch.nn.Conv2d(10, qk_channels * 4, 3)
        self.key = torch.nn.Conv2d(10, qk_channels * 8, 3)
 
    def forward(self, x):
        # Query
        query = self.query(x)
        # Key
        key = self.key(x)
 
        # Dot product
        v1 = torch.einsum("bchw,bhwn->bcwhn", (query, key))
        v2 = v1 / (4 * math.pi**0.5 * math.sqrt((3*qk_channels)**2))
        return v2
