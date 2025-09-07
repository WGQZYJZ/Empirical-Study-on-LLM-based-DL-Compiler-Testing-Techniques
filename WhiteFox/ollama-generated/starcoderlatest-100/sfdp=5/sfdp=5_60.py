
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, qk, v, k, v_dropout, attn_mask, dropout_p):
        # Compute the dot product of the query and key, and scale it
        qk = qk @ torch.transpose(v, -2, -1) / math.sqrt(q.size(-1))
        qk += attn_mask  # Add the attention mask to the scaled dot product
 
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
 
        value = attn_weight @ v  # Compute the dot product of the dropout output and the value
        return output
 


# Inputs to the model
qkv  = torch.randn(1, 3, 64, 64)
