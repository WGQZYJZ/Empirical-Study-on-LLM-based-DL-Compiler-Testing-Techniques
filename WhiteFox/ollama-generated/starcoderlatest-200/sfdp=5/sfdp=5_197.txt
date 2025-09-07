
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, num_layers=6):
        super().__init__()
        self.attn_head = torch.nn.ModuleList()

        for i in range(num_layers):
            self.attn_head.append(
                torch.nn.MultiheadAttention(dim_k=128, dim_v=512, num_heads=num_heads)
            )
    
    def forward(self, query, key, value):
        attn = None
        for i in range(len(self.attn_head)):
            output, attn = self.attn_head[i](query, key, value, output=attn)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(20, 8, 16, 56)
key = torch.randn(20, 8, 32, 48)
value = torch.randn(20, 8, 32, 48)
