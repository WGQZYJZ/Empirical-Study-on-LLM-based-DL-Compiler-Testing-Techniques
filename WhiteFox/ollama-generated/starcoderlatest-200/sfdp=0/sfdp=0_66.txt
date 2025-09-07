
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale):
        dot  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = dot.softmax(dim=-1) # Compute the softmax of scaled dot-product attention
        output = attention_weights.matmul(value) # Multiply the result of the previous step with the value tensor
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, query, key, value, inv_scale):
        v1 = self.attention(query, key, value, inv_scale)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 8, 128, 128) # Input from the encoder of a Transformer model
key   = torch.randn(16, 8, 32,   32) # Input from the encoder of a Transformer model
value = torch.randn(16, 8, 512,  512) # The encoded self-attention output tensor
inv_scale = torch.tensor(1/math.sqrt(16))
