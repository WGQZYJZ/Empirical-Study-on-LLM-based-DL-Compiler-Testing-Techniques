
class Model(torch.nn.Module):
    def __init__(self, num_heads, attn_dropout_p=0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm([3])
        self.attn1 = MultiheadAttention(num_heads)
        self.norm2 = nn.LayerNorm([8])
        self.attn2 = MultiheadAttention(num_heads)
        self.fc1  = nn.Linear(512, 256)
        self.relu = torch.nn.ReLU()
        self.dropout = torch.nn.Dropout(attn_dropout_p)
 
    def forward(self, x):
        # Batch norm
        batch_norm1 = self.norm1(x)
        # Compute the scaled dot product of the query and key (plus an attention mask), followed by a dropout operation
        attn_weights = self.attn1(query=batch_norm1, key=batch_norm1, mask=None)  # Use None to not specify the mask parameter in forward()
        attn_weights = self.dropout(attn_weights)
        # Batch norm
        batch_norm2 = self.norm2(batch_norm1 * attn_weights)
        # Compute the scaled dot product of the dropout output and the value
        outs = self.attn2(query=batch_norm2, key=batch_norm1, value=batch_norm2)  # Use None to not specify the mask parameter in forward()
        outs = self.dropout(outs)
        # Project the output to a single dimension
        return torch.matmul(batch_norm2, attn_weights).view(-1, batch_norm2.shape[-1])


# Initializing the model
m = Model()


