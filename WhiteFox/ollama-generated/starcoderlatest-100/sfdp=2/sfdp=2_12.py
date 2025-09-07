
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        self.linearq = torch.nn.Linear(d_model, num_heads * d_model)
        self.linearb  = torch.nn.Linear(num_heads * d_model, d_model)
        self.lineark  = torch.nn.Linear(d_model, num_heads * d_model)
 
        self.dropout1 = torch.nn.Dropout(dropout)
        self.dropout2 = torch.nn.Dropout(dropout)
 
    def forward(self, q, k, v):
        # q, k and v shape: (batch size, num_heads, length of the sequence, model dimensionality)
        batch_size = q.shape[0]
 
        d_k = q.shape[-1]  # The dimensionality of each head
        d_v = v.shape[-1]
        
        residual = q
    
        linearq = self.linearq(q).view(batch_size, -1, num_heads, d_k)
        linearb  = self.linearb(self.dropout2(torch.nn.functional.gelu(linearq))).view(batch_size, -1, d_v)

        lineark = self.lineark(k).view(batch_size, -1, num_heads, d_k)
        logits  = torch.matmul(linearb, lineark.transpose(-2, -1))
 
        scaled_logits = logits / math.sqrt(d_k)
    
        softmax_logits = self.softmax(scaled_logits)
        
        dropout_softmax_logits = self.dropout(softmax_logits)
        
        output = dropout_softmax_logits.matmul(v).view(batch_size, -1, d_v)
        
        return linearq + linearb + lineark
    
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, attention_dropout=0.,
                 dropout=0., bucket_size=-1, key_padding_value=0):
        super().__init__()
 
        assert embed_dim % num_heads == 0
 
        self.num_buckets = int(embed_dim / num_heads)
 
        if key_padding_value is None:
            key_padding_value = -1

        self.attention = MultiHeadSelfAttention(embed_dim, num_heads,
                                                attention_dropout)
        self.output = torch.nn.Linear(embed_dim, embed_dim)

        self.positional_encoder = PositionalEncoding(
            d_model=embed_dim, max_len=bucket_size + 1, dropout=0.)

        # Positional encodings are added to the embedding vectors
        # and multiplied by the square root of the number of heads, for instance
        # 'sin' is applied to a vector with shape [100, 32] and a position encoding
        # will be created that encodes positions in [0, 100)
        self.dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, enc_input, pos_enc):
        x = self.output(enc_input + pos_enc * self.positional_encoder(pos_enc))
        return self.attention(x, x, x)
 
    def softmax(self, enc_input):
        softmax_values = torch.nn.functional.softmax(enc_input, dim=-1)
        attention_map  = softmax_values * (1 - 1e-8)
        return attention_map
 
# class PositionalEncoding(torch.nn.Module):
    # def __init__(self, d_model, max_len=50, dropout=0.,):
        # super().__init__()
        # self.dropout = torch.nn.Dropout(p=dropout)
        # pe = torch.zeros(max_len, d_model)
        # position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        # div_term = torch.exp(torch.arange(0, d_model, 2) * -(math.log(10000.0) / d_model))
        # pe[:, 0::2] = torch.sin(position * div_term)
        # pe[:, 1::2] = torch.cos(position * div_term)
        # self.register_buffer('pe', pe)
 
    def forward(self, x):
        # pe shape: (batch size, length of the sequence, dimensionality)
        pe = self.pe[:x.shape[1], :].to(x.device)
        return torch.nn.functional.dropout(x + pe, p=0.3, training=False)
        
# class PositionalEncoding(torch.nn.Module):
    # def __init__(self, d_model: int, max_len: int = 50):
        # super().__init__()
 
        # self.pe = torch.zeros(max_len + 1, d_model)
        # position = torch.arange(0, max_len).unsqueeze(1)
 
    # def forward(self, x: torch.Tensor):
        # # pe shape: (batch size, length of the sequence, dimensionality)
        # # return a tensor with positional encodings, added to the inputs
        # if self.pe is None:
            # # initalize the pe matrix
           
// Set up two variables for plotting
let total_time = 0;
const test = async ( ) => {
    let results = [];
    await new Promise(resolve => setTimeout(function() {
      console.log('The time is now ' + Date.now()); // Wed!
      resolve();
    }, 150));
  }
