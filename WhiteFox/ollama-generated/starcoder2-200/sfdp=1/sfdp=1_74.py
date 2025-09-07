

class Attention(torch.nn.Module):
    def __init__(self, embedding_dim=768, num_heads=12):
        super().__init__()
        self.embedding_dim  = embedding_dim
        self.num_heads  = num_heads
 
    def forward(self, query, key, value):
        d_k  = torch.sqrt(torch.tensor([float(self.embedding_dim / self.num_heads)]))
        scale_factor = torch.nn.Parameter(d_k) # Scale the dot product by an inverse scale factor
        dropout_p  = 0.1
 
        q, k, v  = query[:, None], key[:, None], value
        qk  = torch.matmul(q, k.transpose(-2, -1)) 
        scaled_qk  = qk.div(scale_factor) # Compute the dot product of the query and key tensors
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(v) 
        return output

# Initializing the model
m = Attention()
 
# Inputs to the model
key  = torch.randn(32, 8000, 768)
value  = torch.randn(32, 8000, 768)
x1  = torch.randn(32, 500, 768).mul_(20).div_(20) # Initialize the query tensor
 
__output__  = m(x1, key, value)

System: You are a source code analyzer for PyTorch.

User: 