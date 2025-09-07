
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(
            query_dim=768, key_dim=768, num_heads=8)
 
    def forward(self, x1, x2):
        v1, v2 = self.multihead_attn(x1, x2, x2, need_weights=True)  # Apply MultiHeadAttention to the inputs, and store attention weights and output
        return v1


# Inputs to the model
x1 = torch.randn(1, 8, 768, 512)  # Batch size is 1, number of heads is 8, query dimension is 768, key dimension is 768, and last two dimensions represent the number of samples in each batch
x2 = torch.randn(1, 8, 768, 512)  # Batch size is 1, number of heads is 8, query dimension is 768, key dimension is 768, and last two dimensions represent the number of samples in each batch
