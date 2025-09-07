
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tensor_a = torch.full([3], 2.5, dtype=dtype, device=device)
        self.tensor_b = torch.full([4], 0.76, dtype=dtype, device=device)
        self.tensor_c = torch.cumsum(self.tensor_b, dim=[-1])
 
    def forward(self, x):
        v1 = self.tensor_a + self.tensor_b
        v2 = v1 * 0.76
        v3 = v2 * 1
        return v3


# Inputs to the model
__input__ = torch.randn(4, 5)
