

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self._dropout  = torch.nn.Dropout(config['dropout'])
        self._scale  = math.sqrt(config['hidden_size'])
 
    def forward(self, query, key, value, attention_mask=None):
        qk  = query @ key.transpose(-2, -1) / self._scale 
        if attention_mask is not None:
            qk += attention_mask 
 
        attn_weights  = torch.softmax(qk, dim=-1) 
        attn_weights  = self._dropout(attn_weights)
 
        output  = attn_weights @ value 
        return output

class TransformerModel(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.token_embedder  = TokenEmbedding(config['vocab'], config['d_model']) 
        self.position_embedder  = PositionalEncoding(config['maxlen'], config['d_model']) 
 
 
        self._encoder = EncoderLayer(config) 
        self._decoder  = DecoderLayer(config) 
        self.generator  = torch.nn.Linear(config['d_model'], config['vocab']) 
 
    def forward(self, src):
        memory_key_values  = [] 
        src = self.token_embedder(src) 
        src = self._dropout(src) 
        positioned  = self.position_embedder(src) 
        output  = self._encoder(positioned, None)[0] 
        return self.generator(output[:, -1]).unsqueeze(-2).log_softmax()
