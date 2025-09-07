
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2):
        qk = self.attn(x1, x2)[0]
        return qk


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Query Tensor (batch size = 1; num heads = 8; seq len_q = seq len_kv = 64)
x2 = torch.randn(1, 3, 64, 64) # Key Tensor   (batch size = 1; num heads = 8; seq len_k = seq len_v = 64)


