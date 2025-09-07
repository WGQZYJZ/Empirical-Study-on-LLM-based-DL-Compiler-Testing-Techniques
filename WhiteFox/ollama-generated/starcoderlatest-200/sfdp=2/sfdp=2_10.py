
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_attention_heads=8, attention_head_size=64, dropout_p=0.1):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.attention_head_size = attention_head_size
        self.attention_dropout = torch.nn.Dropout(p=attention_dropout)
        self.scaling = torch.nn.Linear(self.attention_head_size, 1, bias=False)
 
    def forward(self, query, key, value):
        # Apply attention dropout to the query, key and values
        projected_query = self.attention_dropout(query)
        projected_key   = self.attention_dropout(key)
        projected_value = self.attention_dropout(value)
 
        scaled_query  = self.scaling(projected_query).unsqueeze(-1)
        scaled_key    = self.scaling(projected_key).unsqueeze(0)
        scaled_values = self.scaling(projected_value).transpose(2, 3)
 
        # Compute the dot product of the query and key
        qk = torch.matmul(scaled_query, scaled_key)

        # Scale the dot product by the inverse scale factor
        scaled_qk = qk.div(inv_scale_factor)
        
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(-1).type_as(qk)
 
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=attention_dropout)
 
        # Compute the dot product of the attention output with the value
        output = dropout_qk.matmul(scaled_values)

        # Multiply the final result by the square root of the number of attention heads to get a context vector for each head
        context = torch.nn.functional.linear(output, self.attention_head_size).transpose(2, 3)

        return context
# Initializing the model
m = MultiHeadAttention()

# Inputs to the model
query = torch.randn(1024, 8, 56, 56)
key   = torch.randn(1024, 8, 28, 28)
value = torch.randn(1024, 8, 28, 28)
