
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_attention_heads: int = 8, attention_head_size: int = 64):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.attention_head_size = attention_head_size

        self.query = torch.nn.Linear(self.attention_head_size * self.num_attention_heads, self.attention_head_size)
        self.key = torch.nn.Linear(self.attention_head_size * self.num_attention_heads, self.attention_head_size)
        self.value = torch.nn.Linear(self.attention_head_size * self.num_attention_heads, self.attention_head_size)
 
    def transpose_for_scores(self, x):
        new_x_shape = x.size()[:-1] + (
            self.num_attention_heads,
            self.attention_head_size,
        )
        x = x.view(*new_x_shape)
        return x.permute(0, 2, 1, 3).contiguous()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        query = self.transpose_for_scores(query)
        key = self.transpose_for_scores(key)
        value = self.transpose_for_scores(value)
 
        # Calculate the attention weights
        energy = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.attention_head_size)
        
        attn_weights = torch.softmax(energy, dim=-1)
        
        # Multiply the attention weight to get context vector
        context_vector = torch.matmul(attn_weights, value)
 
        output = self.transpose_for_scores(context_vector)
        return output


class Model(torch.nn.Module):
    def __init__(self, num_attention_heads: int, attention_head_size: int):
        super().__init__()
        self.multi_head_attn = MultiHeadAttention(num_attention_heads, attention_head_size)
 
    def forward(self, input1: torch.Tensor, input2: torch.Tensor, input3: torch.Tensor):
        # Attention calculation.
        x = self.multi_head_attn(input1, input2, input3)
 
        return x


# Initializing the model
m = Model(4, 64)

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
x2 = torch.randn(8, 64, 64)
x3 = torch.randn(8, 8, 64, 64)
