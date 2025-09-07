
class Model(torch.nn.Module):
    def __init__(self, hidden_size=1024):
        super().__init__()
 
        # Input dimension 3 * 64 * 64 = 98304
        # Output dimension: 1024
        self.layer_1 = torch.nn.Linear(in_features=98304, out_features=hidden_size)
        # Output dimension: 1024
        self.layer_2 = torch.nn.Linear(in_features=hidden_size, out_features=hidden_size)
        # Output dimension: 1024
        self.layer_3 = torch.nn.Linear(in_features=hidden_size, out_features=98304)
 
    def forward(self, x1):
        batch_size = x1.shape[0]
 
        v1 = x1.view(batch_size, -1).unsqueeze(-1) # Input: 98304 * (256*64*64/3)*3 -> Output: 98304 * 98304 * 3
        # Output dimension: batch size x hidden dimension = 256 * 64 * 64
        v2 = self.layer_1(v1)
        # Output dimension: batch size x output dimension= 256 * 64 * 64
        v3 = F.relu(self.layer_2(v2))
        # Output dimension: batch size x hidden dimension = 1024
        v4 = self.layer_3(v3)
 
        return v4.view(batch_size, -1)
 
class DecoderLayer(torch.nn.Module):
    def __init__(self, decoder_dim=512, attention_heads=8):
        super().__init__()
 
        # Dimension of the hidden states produced by each layer in the transformer model
        self.decoder_dim = decoder_dim
 
        # Number of heads used for multi-head attention in the transformer model
        self.attention_heads = attention_heads
 
        self.attn_layer = MultiHeadAttention(num_attention_heads=self.attention_heads, key_dim=self.decoder_dim)
 
        self.ff_layer = torch.nn.Sequential(
            # Input dimension: 256 x 1024
            torch.nn.Linear(in_features=1024 * 3, out_features=4*self.decoder_dim),
            # Output dimension: batch size x input dimension
            torch.nn.Dropout(dropout_p=dropout_p),
            # Activation function: ReLU
            F.relu(),
            # Input dimension: output dimension x hidden dimension = 256 x 1024
            torch.nn.Linear(in_features=4*self.decoder_dim, out_features=self.decoder_dim),
            # Output dimension: batch size x input dimension = batch size x 256 x 1024
            torch.nn.Dropout(dropout_p=dropout_p)
        )
 
    def forward(self, src):
 
        # Input dimension: batch size x hidden dimension = 1 x 256 * 1024
        q, k, v = self.attn_layer(src, src, src)
 
        # Dimension of the hidden states produced by each layer in the transformer model
        decoder_dim = self.decoder_dim
 
        src = torch.transpose(src, -1, -2) # Input: batch size x 256 * 1024*3 -> Output: batch size x 1024*256 x 3
        # Input dimension: batch size x input dimension= 1 x input dimension = batch size x 1024 x 256 * 3
        src_output = torch.transpose(self.ff_layer(torch.cat([src, q, k, v], dim=-1)), -1, -2)
 
        # Output: batch size x 256 * 1024*3
        return src_output
 
class TransformerDecoder(torch.nn.Module):
    def __init__(self, decoder_dim=512, attention_heads=8, layers=4):
        super().__init__()
 
        self.decoder_layers = torch.nn.ModuleList([
            DecoderLayer(decoder_dim, attention_heads) for _ in range(layers)
        ])
 
    def forward(self, src):
        # Input dimension: batch size x 1024 * 1 x 3
        for layer in self.decoder_layers:
            # Output: batch size x 256 * 1024*3
            output = layer(src)
 
        return torch.transpose(output, -1, -2)
 
class Decoder(torch.nn.Module):
    def __init__(self, decoder_dim=512, attention_heads=8, layers=4):
        super().__init__()
 
        # Output dimension: batch size x 1024 * 3
        self.decoder = TransformerDecoder(
            decoder_dim=decoder_dim,
            attention_heads=attention_heads,
            layers=layers)
 
    def forward(self, src):
 
        # Input dimension: batch size x 256 * 98304*1
        output = self.decoder(src)
 
        # Output dimension: batch size x hidden dimension = 1 x 1024 * 3
        output = torch.transpose(output, -1, -2)
 
 
