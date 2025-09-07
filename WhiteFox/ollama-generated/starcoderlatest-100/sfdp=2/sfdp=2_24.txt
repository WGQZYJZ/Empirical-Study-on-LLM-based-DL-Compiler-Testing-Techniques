
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_output = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x1):
        v1 = self.attention_output(x1).mul(0.5) # Multiply the output of attention with 0.5 
        return v1
 

# Initializing the model
m = Attention()
m.to(device)


# Inputs to the model
q = torch.randn(2, 3, 64, 64).to(device) # Shape (batch_size, head_num, query_seq_len, key_seq_len)
k = torch.randn(2, 3, 64, 64).to(device)
v = torch.randn(2, 3, 64, 64).to(device) # Shape (batch_size, head_num, query_seq_len, key_seq_len)
query = q.permute(0, 1, 3, 2).contiguous() # Shape (batch_size, head_num, query_seq_len, key_seq_len)
key = k.permute(0, 1, 3, 2).contiguous()
value = v.permute(0, 1, 3, 2).contiguous() # Shape (batch_size, head_num, query_seq_len, key_seq_len)
query = query.reshape(-1, 8) # Shape (batch_size * head_num * query_seq_len, 8)
key = key.reshape(-1, 8)
value = value.reshape(-1, 8) # Shape (batch_size * head_num * query_seq_len, 8)


