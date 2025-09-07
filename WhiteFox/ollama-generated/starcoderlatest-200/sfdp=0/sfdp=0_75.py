
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, temperature=1):
        super().__init__()
        self.temperature = temperature
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / (inv_scale * self.temperature)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


class SelfAttentionWithMultiHead(torch.nn.Module):
    def __init__(self, d_model=64, num_heads=2, dropout_rate=0.3):
        super().__init__()
        self.num_heads = num_heads
 
        d_qkv = d_model // num_heads
        self.scale  = 1 / math.sqrt(d_qkv)
 
        self.attention_layer = nn.ModuleList([
            nn.Linear(in_features=d_model, out_features=d_qkv * 3),
            ScaledDotProductAttention(),
            nn.Linear(in_features=d_model, out_features=d_model),
        ])
 
        self.norm1 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(p=dropout_rate)
 
        self.linear2 = nn.Linear(in_features=d_qkv, out_features=num_heads * d_qkv)
 
    def forward(self, x):
        y = []
        for attn_layer in self.attention_layer:
            h  = self.norm1(x)
            w1 = self.linear2(attn_layer[0](h))
            y.append(w1)
 
        y = torch.cat(y, dim=-1)
        y = torch.transpose(y, -1, -2).contiguous().view(*y.shape[:-1], num_heads * d_qkv)
        y = self.dropout1(F.gelu(y))
 
        return F.softmax(self.linear2(y), dim=-1)
 
 
class TransformerEncoderLayer(nn.Module):
    def __init__(self,
                 input_dim: int,
                 output_dim: int,
                 intermediate_dim: Optional[int]=None,
                 activation: Optional[str]='gelu',
                 dropout_rate=0.3,
                 use_layer_norm=True,
                 layer_norm_eps: float=1e-5):
        super().__init__()
        if not intermediate_dim:
            self.fc = nn.Linear(input_dim, output_dim)
        else:
            self.fc = nn.Sequential(
                nn.Linear(input_dim, intermediate_dim),
                getattr(F, activation)(),
                nn.Linear(intermediate_dim, output_dim)
            )
 
        self.use_layer_norm = use_layer_norm
        if self.use_layer_norm:
            self.LayerNorm = nn.LayerNorm(output_dim, eps=layer_norm_eps)
        else:
            self.LayerNorm = lambda x: x
 
        self.dropout1 = nn.Dropout(p=dropout_rate)
 
    def forward(self, x):
        output = self.fc(x)
 
        if self.use_layer_norm:
            output = self.LayerNorm(output + x)
        else:
            output += x
 
        return self.dropout1(F.gelu(output))
 
 
class TransformerEncoder(nn.Module):
    def __init__(self, layer, num_layers, d_model=64, dropout_rate=0.3):
        super().__init__()
        self.layer = nn.ModuleList([
            TransformerEncoderLayer(
                input_dim  =d_model,
                output_dim =d_model,
                intermediate_dim=(d_model * 4) if (d_model * 4 < d_model * 2048) else None,
                dropout_rate=dropout_rate
            ) for i in range(num_layers)
        ])
 
    def forward(self, x):
        for layer_block in self.layer:
            x = layer_block(x)
 
        return x
 

class ModelWithTransformerEncoder(nn.Module):
    def __init__(self, d_model=64, nhead=2, num_layers=6, output_dim=3072, dropout_rate=0.1):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.num_layers = num_layers
 
        self.embedding = nn.Embedding(589, d_model)
 
        encoder_layer = TransformerEncoderLayer(
            input_dim=d_model,
            output_dim=d_model,
            intermediate_dim=(d_model * 4) if (d_model * 4 < d_model * 2048) else None,
            dropout_rate=dropout_rate
        )
 
        self.transformer = TransformerEncoder(layer=encoder_layer, num_layers=num_layers)
 
        self.fc = nn.Sequential(
            nn.Linear(d_model * 3, output_dim),
            nn.ReLU(),
            nn.Linear(output_dim, output_dim),
        )
 
    def forward(self, x):
        z1 = self.embedding(x).unsqueeze(0)
 
        out1 = self.transformer(z1)
 
        y = torch.transpose(out1[0], -1, -2)
 
        z1 = torch.cat((out1[0], y, out1[-1]), dim=-1)
        output = self.fc(z1).view(-d))
