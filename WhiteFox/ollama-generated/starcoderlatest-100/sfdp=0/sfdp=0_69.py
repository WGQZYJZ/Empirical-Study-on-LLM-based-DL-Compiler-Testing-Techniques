
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk_raw, kv_raw):
        # Input: Q K V (batch x timesteps x ... x channels)
        batch = qk_raw.shape[0]
        key, value = kv_raw
        
        # Calculate the scaling factor inv_scale
        inv_scale  = torch.sqrt(torch.tensor(float(key.shape[-1])).to(device))
        scaled_dot_product  = torch.matmul(qk_raw, key.transpose(-2, -1)) / inv_scale
 
        # Calculate the attention weights using softmax and apply them to all the values
        attention_weights = scaled_dot_product.softmax(dim=-1)

        output = attention_weights.matmul(value)
        return output
        
# Initializing the model
m = ScaledDotProductAttention()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = ScaledDotProductAttention()
 
    def forward(self, x1):
        v1 = self.conv(x1)

        # (batch size x length of input sequence x embedding dim)
        q_k_v = torch.cat((q_raw, k_raw), dim=2)
        v2 = self.attention(q_k_v, v_raw)
 
        return output
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
output = m(x1)


