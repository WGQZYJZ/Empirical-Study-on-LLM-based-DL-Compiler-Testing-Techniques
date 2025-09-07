
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_linear = torch.nn.Linear(768, 1024)
        self.fc = torch.nn.Linear(1024, 768)
 
    def forward(self, x1, x2, attn_mask):
        qk  = torch.matmul(x1, self.qkv_linear.weight).transpose(-1, -2) # Compute the dot product of the query and key
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = torch.matmul(attn_weight, x2) # Compute the dot product of the dropout output and the value
        output = self.fc(output)
        return output


# Initializing the model
m = AttentionModel()
# Inputs to the model
x1 = torch.randn(4, 3, 768) # query tensor with shape (B, C_in, H_q, W_q)
x2 = torch.randn(5, 8, 768) # key tensor with shape (B, C_out, H_k, W_k)
attn_mask = torch.ones((1024,), device='cuda')
