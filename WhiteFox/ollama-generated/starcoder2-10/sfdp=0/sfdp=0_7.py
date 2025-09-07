
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.scale = torch.rsqrt(torch.tensor([dim]))
 
    def forward(self, query, key, value):
        scaled_dot  = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        attention_weights  = scaled_dot.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(32, 64, 512).cuda()
        self.key  = torch.randn(32, 64, 512).cuda()
        self.value  = torch.randn(32, 64, 512).cuda()
 
        self.scale  = torch.rsqrt(torch.tensor([512]))
 
        self.self_attention = ScaledDotProductAttention(dim=512)
 
    def forward(self):
        scaled_dot  = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        attention_weights  = scaled_dot.softmax(dim=-1)
        output  = attention_weights.matmul(value)
