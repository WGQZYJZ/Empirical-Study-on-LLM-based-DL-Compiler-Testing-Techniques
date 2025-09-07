
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, input_dim: int, num_heads: int):
        super().__init__()
        self.input_dim = input_dim
        self.num_heads = num_heads
 
        # Compute dimension of head
        self.head_dim = input_dim // num_heads
 
        # Number of linear transformations in the multi-head attention block, i.e., (num_heads * 2) + output dim 
        self.multiheadattentionblockdim = (
            num_heads * 2 + input_dim
        )
 
    def forward(self, x1):
        h1 = torch.nn.Linear(x1.size(-1), self.multiheadattentionblockdim)(x1)
 
        q1, k1, v1 = torch.split(h1, self.head_dim, dim=-1)
        # Compute the dot product of the query and key, and scale it
        qk  = q1 @ k1.transpose(-2, -1) / math.sqrt(q1.size(-1))
        qk += attn_mask  # Add the attention mask to the scaled dot product
 
        attn_weight  = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = (
            attn_weight @ v1  # Compute the dot product of the dropout output and the value
        )
        
        output = torch.cat([q1, output], dim=1)
 
        return output
 
    def num_parameters(self):
        return self.multiheadattentionblockdim
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # Number of heads
        self.num_heads = 4
 
        # MultiHeadAttention layer with input dim=768, num_heads=8
        self.mha = MultiHeadAttention(input_dim=1280, num_heads=self.num_heads)
 
    def forward(self, x1):
        h1 = torch.nn.Linear(x1.size(-1), 1280)(x1)
 
        h2 = self.mha(h1)
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 4, 768, 64)
 
 