
class Model(torch.nn.Module):
    def __init__(self, embedding_dim: int, num_heads: int, d_model: int):
        super().__init__()
        self.inv_sqrt_embed_dim = 1 / math.sqrt(embedding_dim)
 
        self.attn_layer_q = torch.nn.Linear(embedding_dim * 3, embedding_dim)
        self.attn_layer_k = torch.nn.Linear(embedding_dim * 3, embedding_dim)
        self.attn_layer_v = torch.nn.Linear(embedding_dim * 3, embedding_dim)
 
        self.dense_layer = torch.nn.Linear(d_model, d_model)
 
    def forward(self, x1):
        q1 = self.inv_sqrt_embed_dim * (self.attn_layer_q(x1))
        k1 = self.inv_sqrt_embed_dim * (self.attn_layer_k(x1))
        v1 = self.inv_sqrt_embed_dim * (self.attn_layer_v(x1))
 
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(q1.size(-1))
 
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(v1)
 
        return self.dense_layer(output)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
