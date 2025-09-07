
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=4, num_attention_heads=16)
 
    def forward(self, q, k, v):
        output, _  = self.attention(q, k, value=v)
        return output


# Initializing the model
m = Model()
q = torch.randn(20, 512, 384, requires_grad=True).cuda().float()
k = torch.randn(16, 512, 192, requires_grad=True).cuda().float()
v = torch.randn(16, 512, 192, requires_grad=True).cuda().float()

