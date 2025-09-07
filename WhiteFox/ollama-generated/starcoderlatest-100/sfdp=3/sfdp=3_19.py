
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, hidden_size, num_heads=8, scale_factor=0.75):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.scale_factor = scale_factor
        head_size = hidden_size // num_heads
 
        self.head_projection = torch.nn.Linear(self.hidden_size, head_size * num_heads)
        self.combine_attention = torch.nn.Linear(head_size * num_heads, hidden_size)
 
    def forward(self, query, key, value):
        batch_size = query.shape[0]
        sequence_length = query.shape[-1]
 
        qk = self.head_projection(query).view(batch_size, -1, self.num_heads, head_size)
        qk = torch.transpose(qk, -2, -3)  # qk is shape (batch_size, num_heads, sequence_length, head_size)
 
        softmax_qk = qk.softmax(dim=-1)  # Softmax along the last dimension, this is shape (batch_size, num_heads, sequence_length, sequence_length)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.scale_factor)
        output = self.combine_attention(dropout_qk).view(batch_size, -1, self.num_heads * head_size)
 
        return output
 
class Model(torch.nn.Module):
    def __init__(self, attention_head_size=256, num_heads=8):
        super().__init__()
        self.attention = MultiHeadAttention(attention_head_size, num_heads, scale_factor=0.75)
 
    def forward(self, query, key, value):
        attention = self.attention(query, key, value)
 
        return attention


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(2, 32, 256, 256)
x2 = torch.randn(2, 32, 256, 256)
x3 = torch.randn(2, 32, 256, 256)
