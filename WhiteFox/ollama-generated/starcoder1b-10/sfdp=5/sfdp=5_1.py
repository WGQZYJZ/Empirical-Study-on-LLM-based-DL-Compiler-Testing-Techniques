
class Model(torch.nn.Module):
    def __init__(self, num_layers=2, num_heads=8):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(512)  # Use layer normalization to align the channels axis of input tensors in a bidirectional feed-forward network
        self.self_attn = SelfAttention(num_layers=num_layers, num_heads=num_heads)
        self.position_embedding = PositionEmbedding(token_emb_size=512, max_len=max_len)
 
    def forward(self, input):
        