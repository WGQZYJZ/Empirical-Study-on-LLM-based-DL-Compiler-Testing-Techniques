
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(20, 32)
        self.norm_qkv = LayerNorm(32)
 
    def forward(self, x1):
        qk = self.qkv(x1).chunk(3, dim=-1)
        dk = torch.exp(qk[0] - kq[1])  # Apply exponential to the queries and keys
        scale_factor = dk * math.sqrt(dk.size(-1))  # Calculate the scale factor for the queries and keys
        qk = qk.div(scale_factor)  # Scale the dot products of the queries and keys by the scale factor
        output = self.norm_qkv(qk).chunk(3, dim=-2) * dk  # Apply pointwise convolution with pointwise kernel size equal to 1
        return torch.cat(output, dim=-1)


# Inputs to the model
x1 = torch.randn(1, 20, 5, 5)
