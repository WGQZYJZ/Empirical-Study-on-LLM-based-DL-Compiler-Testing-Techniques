
class Model(torch.nn.Module):
    def __init__(self, embed_size: int = 512, num_heads: int = 8, num_layers: int = 6,
                 dropout_p: float = 0.1, max_len: int = 5):
        super().__init__()
        self.embed = torch.nn.Embedding(num_embeddings=max_len, embedding_dim=embed_size)
        self.attn_head = TransformerEncoderLayer(embed_size=embed_size, num_heads=num_heads, dropout_p=dropout_p)
        self.fc1 = torch.nn.Linear(in_features=embed_size*2, out_features=embed_size, bias=False)
        self.norm = torch.nn.LayerNorm(embed_size, eps=1e-8)
        self.drop = torch.nn.Dropout(dropout_p)
        self.fc2 = torch.nn.Linear(in_features=embed_size, out_features=max_len, bias=False)
 
    def forward(self, input_tensor):
        batch_size, src_seq_len, embed_dim = input_tensor.shape
        x1 = self.embed(input_tensor).transpose(0, 1).contiguous().view(-1, src_seq_len, embed_dim)
        attn_out = F.gelu(self.attn_head(x1))
        # attn_out: [batch_size, src_seq_len, embed_dim*4]
        output = self.fc1(torch.cat((attn_out, x1), dim=-1)).transpose(-2, -1)  # (bs, src_len, embed_dim*2)
        output = self.norm(output).transpose(-2, -1)  # [batch_size, src_seq_len, embed_dim]
        output = self.drop(F.gelu(self.fc2(output)))  # [batch_size, max_len]
        return F.softmax(output, dim=-1).view(-1, src_seq_len)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(128, 3, 64, 64)
