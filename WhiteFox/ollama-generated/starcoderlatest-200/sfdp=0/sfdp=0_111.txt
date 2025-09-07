
class Attention(torch.nn.Module):
    def __init__(self, dim, num_heads = 128):
        super().__init__()
        self.num_heads = num_heads
        self.dim = dim
        self.proj_qkv = torch.nn.Linear(dim, dim * 3, bias=False)
 
    def forward(self, x):
        batch_size = x.shape[0]
 
        qkv = (
            self.proj_qkv(x).chunk(2, dim=-1)
            + (batch_size, self.num_heads, 1, 1)
            + torch.arange(
                0,
                batch_size * self.num_heads,
                dtype=torch.long,
                device=x.device,
            )
        ).flatten(2).transpose(-2, -3)
 
        qkv = qkv.contiguous().view(*qkv.shape[:2], 3, self.dim)
        q, k, v = qkv[0].float(), qkv[1].float(), qkv[2].float()
        
        attention_weights = (
            torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.dim)
        ).softmax(dim=-1)
 
        output = (attention_weights * v).sum(dim=0)
 
        return output
 
 
class Model(torch.nn.Module):
    def __init__(self, dim=512, num_heads=64):
        super().__init__()
        self.embedding = torch.nn.Embedding(
            30000,
            embedding_size,
            padding_idx=pad_token_id,
        )
 
        self.encoder = Encoder(EncoderLayer(dim, dim, num_heads))
        self.attention = Attention(dim)
        self.projection = torch.nn.Linear(dim, 30000)
 
    def forward(self, x):
        # Add hidden state as an input to the first layer
        hiddens = (x, None)
 
        # Embedding and encoding of input sequences. 
        # We add a dimension for the sequence length in the embedding layer.  
        # The output shape is `(batch_size, seq_len, embed_dim)`.
        embeddings = self.embedding(x) 
        encoded_embeddings = self.encoder(hiddens).last_hidden_state
 
        # Pass the encoded sequences to an attention layer
        attention_output = self.attention(encoded_embeddings)
 
        # Project the representation of each sequence in the batch to their final representations by a linear layer
        logits = self.projection(attention_output)
 
        return logits
 

# Initializing the model and checking the dimension of weights
m = Model()
 
print('Size of qkv weight: ', m.embedding.weight.size())  # (30000, embedding_dim, embed_dim)
print('Size of projected embedding layer: ', m.projection.in_features) # 30000
# Size of qkv weight:  torch.Size([30000, 512, 512])
# Size of projected embedding layer:  30000


