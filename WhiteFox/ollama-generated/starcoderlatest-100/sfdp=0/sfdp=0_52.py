
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim=1024, num_heads=16):
        super().__init__()
        self.head = torch.nn.Linear(embed_dim, embed_dim)  # linear transformation for each head

    def forward(self, query, key, value, mask):
        # Compute the dimensions of the input tensors.
        batch_size, q, k, v = [s if s > 0 else 1 for s in (query.shape[0], key.shape[-2], key.shape[-1], value.shape[-1])]
        n_heads, e_head = query.shape[-2], query.shape[-1]

        # Reshape the input tensor to [batch_size x q x e_head].
        query = query.reshape(batch_size, q, n_heads, e_head)
        key = key.reshape(batch_size, k, n_heads, e_head)
        value = value.reshape(batch_size, v, n_heads, e_head)

        # Compute the attention weights between all query and key tensors.
        qk_weights  = torch.einsum('bahd,bhda->bahd', query, self.head)

        # Apply a mask to prevent attention from looking at future timesteps when computing the weighted sum of the value tensor.
        if mask is not None:
            qk_weights += (1e9 * mask).detach()

        # Normalize the attention weights for each head and sum them up.
        qk_weights = qk_weights / torch.sqrt(float(e_head))
        qk_weights = torch.sum(qk_weights, dim=-2)  # [batch_size x q]

        # Compute the output tensor from the scaled dot product attention weights and value tensors.
        context = torch.einsum('bahd,bhda->bahd', qk_weights, self.head)

        # Reshape the output tensor back to a form that conforms with the input tensor.
        return context.view(batch_size, q, n_heads * e_head)

class Model(torch.nn.Module):
    def __init__(self, embed_dim=1024, num_heads=8):
        super().__init__()
        self.multihead = MultiHeadAttention(embed_dim=embed_dim, num_heads=num_heads)
 
    def forward(self, x1, mask):
        # Apply multi-head attention to the input tensor. The output tensor is reshaped back into [batch_size x q x e_head].
        v1 = self.multihead(query=x1, key=x1, value=x1, mask=mask)
 
        return v1


# Inputs to the model
x1 = torch.randn(1, 32, 512, requires_grad=True)
mask = torch.ones_like(x1, dtype=torch.float32)
m = Model()
