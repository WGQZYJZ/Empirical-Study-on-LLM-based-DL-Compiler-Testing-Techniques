
class Attention(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q, k, v, scale=1.0):
      # compute scaled dot product of query and key: q shape = (B, N_q, k_dim) / key shape = (B, k_dim, N_k).  Note that the attention_weights tensor is then normalized and used to compute a weighted sum across values of v.
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)

        output  = torch.sum(attention_weights * v, dim=2)
        return output

# Initializing the model