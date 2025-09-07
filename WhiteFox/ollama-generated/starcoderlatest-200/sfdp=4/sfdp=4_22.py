
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_linear = torch.nn.Linear(768, 3 * 32)
 
    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8):
        batch_size  = x1.shape[0]
        nheads      = x2.shape[1]
        head_dim    = x2.shape[-1]
        qkv_dim     = 768

        # Split the inputs into different tensors
        query        = x1.view(batch_size, -1, self.qkv_linear.out_features)
        key          = x3.view(batch_size, -1, self.qkv_linear.out_features)
        value        = x4.view(batch_size, -1, self.qkv_linear.out_features)

        # Split the queries into different tensors for each head in parallel
        qk  = torch.einsum('b n h d, b n d k -> b n h k', query, key).transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it

        # Split the attention mask into different tensors for each head in parallel
        attn_mask = x5.view(batch_size, -1, self.qkv_linear.out_features)

        # Add the attention mask to the scaled dot product
        qk += attn_mask  # Add the attention mask to the scaled dot product
 
        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        # Compute the weighted sum of the values
        output      = torch.einsum('b n h k, b n d v -> b n h v', attn_weight, value).transpose(-2, -1).contiguous().view(batch_size, nheads * head_dim, -1)  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(80, 32, 64, 64)
x2 = torch.randint(low=0, high=32, size=(1, 32))
x3 = torch.randint(low=0, high=64, size=(1, 32, 64, 64))
x4 = torch.randint(low=0, high=64, size=(80, 32, 64))
x5 = torch.randn(80, 32, 768)


