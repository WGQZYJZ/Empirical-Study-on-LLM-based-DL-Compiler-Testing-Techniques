
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value): 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / np.sqrt(key.shape[-1]) 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output   = attention_weights.matmul(value) 
        return output

# Initializing the model
sdaa = ScaledDotProductAttention()

 # Inputs to the model
q = torch.randn([2, 3])
k = torch.randn([4, 5])
v = torch.randn([10, 6])
  