
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            16,
            num_heads,
            stride=16,
            padding=4,
            dropout=0.,
        )
 
    def forward(self, x1, key, value, query, attn_mask):
        _, __output__, __attention__  = self.attn(x1, key, value)
        return __output__
 
 # Initializing the model
m = Model(num_heads=8)

 # Inputs to the model
x1 = torch.randn(16, 16, 32, 32)
key = torch.randn(16, 16, 32, 32)
value = torch.randn(16, 16, 8, 8)
query = torch.randn(16, 16, 16, 16)
attn_mask = torch.ones(16, 16)

 