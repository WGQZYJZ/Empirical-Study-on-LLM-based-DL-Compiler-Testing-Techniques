
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_layer = torch.nn.Linear(512, 1024) # [batch, 512] --> [batch, 1024]

    def forward(self, x):
        qk = self.q_layer(x).view(-1, self.num_heads, self.head_dim)  # (batch, seq_len, num_heads * head_dim) --> [batch*seq_len, num_heads, head_dim] 
        qk = qk / torch.sqrt(self.head_dim)  # Normalization
        softmax_qk = softmax(qk, dim=-1) # Apply softmax to the scaled dot product
        output = dropout(softmax_qk.matmul(self.v), self.dropout) # [batch*seq_len, num_heads, head_dim] --> [batch, seq_len, emb_dim] 
        return output
# Initializing the model
m = Model()


