
class Model(torch.nn.Module):
    def __init__(self, vocab_size: int = 100):
        super().__init__()
        self.embed_query = torch.nn.Embedding(vocab_size, 512) # embed_dim=128, num_embeddings=1024
        self.fc = torch.nn.Linear(512 * 3, vocab_size)
 
    def forward(self, input, key, value):
        qk = (input @ self.embed_query).view(input.size(0), -1, 3, 512).permute(0, 3, 2, 1).contiguous().flatten(0, 1) # embed queries and keys with dim=1
        v  = value.transpose(-2, -1).flatten(0, 1).unsqueeze(dim=-1)  # flatten values
        attn_weight = (qk @ v) / math.sqrt(input.size(-1))  # dot product between query vector and key vector with dim=1 divided by sqrt(value dimension) 
        attn_mask    = torch.arange(0, vocab_size).unsqueeze(dim=-1) <= attn_weight
        attn_weight  = torch.where(attn_mask, torch.ones_like(attn_weight), -1e9 * torch.ones_like(attn_weight)) # set attention weights of masked key vectors to zero
        
        attn_weight = torch.softmax(attn_weight, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output       = attn_weight @ value # compute dot product between the weighted query and the values with attention mask (scaled dot product)
        
        logits = self.fc(output)
        logit  = nn.functional.softmax(logits, dim=-1).unsqueeze(dim=-2) # softmax operation on logits for the classification task

        return output, logits, attn_weight

# Inputs to the model
input   = torch.randint(0, high=vocab_size - 1, size=(48, 60))
key     = torch.randint(0, high=vocab_size - 1, size=(32, 60, 512)) # key is 32 tokens long with a dimension of 512
value   = torch.randn((32, 60, 100))
 
__output__, __logits__, __attn_weight__ = m(input, key, value)
# Attention weights:
