
class SelfAttnQuerySelfAttnKeyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_key(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
        qk = torch.einsum('nc,nd,mc->nm', [x1, v1, v1]) / math.sqrt(v1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
 
        return torch.matmul(attn_weight, v1)
