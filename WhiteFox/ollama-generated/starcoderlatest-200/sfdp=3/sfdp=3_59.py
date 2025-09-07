
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(dim_embed_query, dim_embed_key)
        self.scale_factor = dim_embed_key ** 0.5
        self.attention = torch.nn.Softmax(dim=-1)

    def forward(self, query, key, value):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) * self.scale_factor
        softmax_qk = self.attention(scaled_qk)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p, training=self.training)
        output = torch.matmul(dropout_qk, value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(1, dim_embed_key, 64 * 64)
