
import torch
 
class TransformerLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads=8)
 
    def forward(self, query, key, value, attn_mask):
        out  = self.attn(query, key, value)[0] + query # Compute the scaled dot-product attention mechanism, and add the original query tensor to it
        return torch.nn.LayerNorm()(out) # Apply layer normalization to the output of the Transformer block
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.nn.Linear(embed_dim, embed_dim) 
        self.key    = torch.nn.Linear(embed_dim, embed_dim) # Construct a linear layer to map the input tensor onto the embedding dimension of query and key tensors
        self.value  = torch.nn.Linear(embed_dim, embed_dim)
 
        self.transformerlayer1  = TransformerLayer() 
        self.transformerlayer2  = TransformerLayer()
        self.finallinear         = torch.nn.Linear(embed_dim, vocab_size) # Construct a linear layer to map the output of the transformer block onto the vocabulary size
 
    def forward(self, x):
        qk1  = self.query(x) @ self.key(x).transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask # Compute the dot product of the query and key tensors for each Transformer layer
        attn_weight1 = torch.softmax(qk1, dim=-1) # Apply softmax to the result of the first transformer block
        vq1  = qk @ value 
        vout1  = self.transformerlayer1(vq1)
 
        qk2  = self.query(vout1) @ self.key(vout1).transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask # Compute the dot product of the query and key tensors for each Transformer layer
        attn_weight2 = torch.softmax(qk1, dim=-1)  # Apply softmax to the result of the second transformer block
        vq2  = qk @ value 
        vout2  = self.transformerlayer2(vq2)
 
        out  = self.finallinear(vout2) # Compute the dot product of the attention weights and the value tensor, and then apply a linear layer to it to map the output onto the vocabulary size
        return torch.nn.LayerNorm()(out), qk1 + qk2
 
embed_dim   = 512 
 
vocab_size  = len(vocabulary) # Get the length of the vocabulary
attn_mask  = torch.ones([1, vocab_size])
for i in range(130):
    attn_mask[i][i]  = -math.inf
 
m  = Model()

