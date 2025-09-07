
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_model, nhead=8):
        super().__init__()
        self.nhead = nhead
        # This line of code can only be applied in the forward method. You can't define your own parameter directly on initialization.
        self.qkv  = torch.nn.Linear(dim_model, dim_model * 3, bias=False)
 
    def forward(self, q, k, v, attn_mask):
        # Use nn.Linear to apply the linear transformation. Apply this transformation multiple times on each query, key and value tensor. The output of each application is concatenated along the new dimension (see https://pytorch.org/docs/stable/generated/torch.nn.Linear.html).
        qkv = self.qkv(torch.cat([q, k, v], dim=-1))
        # Split the concatenated outputs by the number of heads and split each element into a head tensor.
        q, k, v = [x.view(-1, self.nhead, x.size(-1) // self.nhead).transpose(0, 1) for x in torch.chunk(qkv, 3, dim=0)]
        # Compute the scaled dot product attention using a scaled dot-product attention mechanism. You can learn more about this pattern on https://arxiv.org/pdf/1706.03762.pdf. 
        # The output of `qk = torch.matmul(q / math.sqrt(v.size(-1)), k)` and `attn_weight = torch.softmax(qk, dim=-1)`, which is a matrix multiply between two tensors whose shapes are the same except for the last dimension (the first dimensions represent the elements in each column). The attention weights computed by this mechanism are stored in the attn_weights tensor.
        qk = torch.matmul(q / math.sqrt(v.size(-1)), k)
        attn_weight = torch.softmax(qk, dim=-1)
        # Compute the weighted sum of the value tensor using the attention weights and return the output. 
        return torch.matmul(attn_weight, v)


class Model(torch.nn.Module):
    def __init__(self, dim_model=32, nhead=8):
        super().__init__()
        self.multi_head_attention = MultiHeadAttention(dim_model, nhead)
 
    def forward(self, x1, x2, attn_mask):
        output  = self.multi_head_attention(x1, x2, x2, attn_mask)
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
attn_mask = torch.randn(1, 1, 64, 64)
