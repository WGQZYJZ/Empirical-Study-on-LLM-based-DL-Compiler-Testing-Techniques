
class Model(torch.nn.Module):
    def __init__(self, hidden_size=256):
        super().__init__()
        self.attn1 = torch.nn.Linear(hidden_size * 3, hidden_size)
        self.attn2 = torch.nn.Linear(hidden_size * 3, hidden_size)
        self.dense1 = torch.nn.Linear(hidden_size, hidden_size)
 
    def forward(self, x1, key, value, query, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        v2 = output.transpose(-1, -2).contiguous().view(output.shape[0], -1)  # Transpose and reshape to (batch size * max_num_attention_heads, hidden_size)
        output = self.dense1(v2) + output  # Add residual connection with the hidden states of the attention heads
        v3 = torch.tanh(output)  # Apply tanh activation function
        attn_output = self.attn1(torch.cat((query, key, v3), dim=-1))
        attn_output = torch.nn.functional.dropout(attn_output, p=dropout_p, training=is_training)
        attn_weight2 = torch.softmax(self.attn2(attn_output), dim=-1)  # Apply softmax to the result
        attn_weight2 = torch.dropout(attn_weight2, dropout_p, True)  # Apply dropout to the softmax output
        v4 = attn_weight2 @ value  # Compute the dot product of the dropout output and the value
        return output + v4
 
    def predict(self, x1):
        