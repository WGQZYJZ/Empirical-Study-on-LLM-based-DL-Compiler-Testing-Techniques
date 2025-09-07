
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(1024, 512)
        self.dropout = torch.nn.Dropout(0.5)
        self.linear2 = torch.nn.Linear(512, 256)
 
    def forward(self, q, k):
        v = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_sqrt = torch.rsqrt(torch.tensor(v.size(-1))).to(device)
        scaled_dot_product = v * inv_scale_sqrt
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(k)
        return output


# Initializing the model
attention = Attention()

 # Inputs to the model
query  = torch.randn(256, 512).to(device)
key    = torch.randn(256, 512).to(device)
