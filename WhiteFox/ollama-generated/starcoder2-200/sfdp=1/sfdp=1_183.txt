
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q, k, v):
         output  = torch.matmul(q, k.transpose(-2, -1)) / sqrt_d_k  # Compute the dot product of the query and key tensors
         output  = output.softmax(dim=-1)  # Apply softmax to the scaled dot product
         output  = F.dropout(output, p=p)  # Apply dropout to the softmax output
         output  = torch.matmul(output, v)
         return output


# Initializing the model
model = Model()

# Inputs to the model
q  = torch.randn(4096, 384, 257) # query tensor shape (sequence length x batch size x embedding dim)
k  = torch.randn(131072, 384, 32) # key tensor shape (num_attention_heads * num_attention_hidden_size x batch size x sequence length)
v  = torch.randn(131072, 384, 512) # value tensor shape (num_attention_heads * hidden dim of multi-head self-attn x batch size x sequence length)


