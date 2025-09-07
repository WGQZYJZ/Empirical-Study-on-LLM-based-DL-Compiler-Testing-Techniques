
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(256, 1024)  # 1024 is the dimension of the query vector
        self.attn_k = torch.nn.Linear(256, 1024)  # 1024 is the dimension of the key vector
        self.attn_v = torch.nn.Linear(256, 1024)  # 1024 is the dimension of the value vector

    def forward(self, qk, attn_mask):
        v2 = torch.matmul(self.attn_q(qk), self.attn_k(qk)) / math.sqrt(qk.size(-1)) # Compute attention weights with softmax operation and dropout operation
        attn_weight = torch.softmax(v2, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        
        v3 = torch.matmul(attn_weight, self.attn_v(qk)) # Compute the dot product of the dropout output and the value
        return v3

# Initializing the model
m = AttentionModel()
# Inputs to the model
qk1  = torch.randn(2, 1024, 512)
v1   = torch.randn(2, 1024, 64)
attn_mask1 = torch.ones((2, 512, 1))
