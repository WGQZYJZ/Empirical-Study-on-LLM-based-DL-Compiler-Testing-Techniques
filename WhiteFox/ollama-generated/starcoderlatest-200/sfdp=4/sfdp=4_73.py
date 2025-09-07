The code snippet in the above cell represents a self-attention mechanism with two linear layers in `query_layer`. Each time when the key tensor and value tensor are both used to compute the attention weights, an additional linear layer is applied to the resulting dot product. This linear layer contains 16 neurons (output of attention mask) to make it more generic for a self-attention mechanism.


# Model
class Attention(torch.nn.Module):
    def __init__(self, q_channel: int=8, v_channel: int=8, attn_head: int=8):
        super().__init__()
        self.query_layer = torch.nn.Linear(q_channel, attn_head * q_channel)  # Linear layer for the query tensor
        self.value_layer = torch.nn.Linear(v_channel, attn_head * v_channel)  # Linear layer for the value tensor
 
    def forward(self, q, k, v):
        v2q = q @ k.transpose(-2, -1) / math.sqrt(k.size(-1)) # Scale the dot product by square-root of key's dimension
        attn_weight = torch.softmax(v2q, dim=-1).unsqueeze(dim=-2)  # Apply softmax to scaled dot product and put it in a tensor with additional dimension for heads
        output = torch.matmul(attn_weight, v).transpose(-2, -1)  # Perform matrix multiplication between attention weights and value to produce attention features
        return output, attn_weight

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = Attention()
 
    def forward(self, x1, x2):
        v1, attn_weight = self.query_layer(x1) # Compute attention weights for the input tensor and the key tensor
        v2, _           = self.query_layer(x2, k=v1, v=attn_weight)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
__output__, __attn_weight__ = m(x1, x2)
