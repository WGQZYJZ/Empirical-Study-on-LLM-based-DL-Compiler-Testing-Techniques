
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.layer_norm1 = torch.nn.LayerNorm([768])
        self.layer_norm2 = torch.nn.LayerNorm([3072])
        self.linear = torch.nn.Linear(768, 3072)
 
    def forward(self, x):
        v1 = self.layer_norm1(x)
        v2 = self.layer_norm2(torch.matmul(v1, self.linear.weight) + v1 * self.linear.bias)
        return v2
