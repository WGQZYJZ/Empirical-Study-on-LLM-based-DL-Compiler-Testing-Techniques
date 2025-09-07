
class MultiheadAttnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_in=768)
 
    def forward(self, x1):
        attention_weights = self.attn(x1, x1, x1)[0]
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = MultiheadAttnModel()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
