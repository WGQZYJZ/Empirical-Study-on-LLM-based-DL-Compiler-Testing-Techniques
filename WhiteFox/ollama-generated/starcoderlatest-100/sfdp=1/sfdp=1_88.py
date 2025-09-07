
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed_dim = embed_dim
        self.head_num = 8
        self.fc1 = torch.nn.Linear(embed_dim, embed_dim)
        self.fc2 = torch.nn.Linear(embed_dim * 3, embed_dim)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / (math.sqrt(self.embed_dim)) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        out1 = self.fc1(output.transpose(-2, -1).contiguous().view(-1, self.embed_dim * 3))  # Apply linear transformations on query and key to produce intermediate tensors
        out2 = self.fc2(out1)  # Apply final linear transformation on the intermediate tensors
        return out2.view(-1, 8, self.embed_dim).transpose(0, 1), output
 

# Initializing the model
m = MultiHeadAttention(512)
x1 = torch.randn(64, 3, 512)
__output__, __out__ = m(x1, x1, x1)

