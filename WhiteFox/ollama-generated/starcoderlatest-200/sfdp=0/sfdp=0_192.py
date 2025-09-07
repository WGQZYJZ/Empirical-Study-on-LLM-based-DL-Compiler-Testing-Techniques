
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32*4*4, 64)
 
    def forward(self, x1, x2, scaled_dot_product=None, attention_weights=None):
        v2 = self.fc1(x1.reshape(-1, 32 * 4 * 4))
        v1 = torch.matmul(v2.view(x2.shape[0], -1), x2) / scaled_dot_product.unsqueeze(-1)
        return v1
 
# Initializing the model
m = Model()


class SelfAttentionNet(nn.Module):
    def __init__(self,
                 embed_size=512,
                 input_dim=4096,
                 nhead=8,
                 num_encoder_layers=6,
                 num_decoder_layers=6,
                 dropout_rate=0.1):
        super().__init__()
        self.layerNorm = nn.LayerNorm(input_dim)

        encoder_layer = TransformerEncoderLayer(d_model=embed_size, nhead=nhead,
                                              dim_feedforward=4 * embed_size)
        decoder_layer = TransformerDecoderLayer(d_model=embed_size, nhead=nhead,
                                              dim_feedforward=4 * embed_size)

        self.transformerEncoder = TransformerEncoder(encoder_layer, num_layers=num_encoder_layers)
        self.transformerDecoder = TransformerDecoder(decoder_layer, num_layers=num_decoder_layers)

        self.fc = nn.Linear(embed_size, input_dim, bias=False)
        
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        x = self.transformerEncoder(x) # 4096 -> 256
        x = x.permute(0, 2, 1) # [B, 256, 4096]
        x = F.layer_norm(x, x.shape[-1], eps=1e-7)

        # for inference only
        v = self.fc(x).unsqueeze(-1)
        
        # inference: no attention weight; masked input or self_attn only
        # encoder output + scaled dot product weights with encoder inputs
        # decoder input (for the last step) + self_attn with encoder inputs + decoder hidden states
        x, v2, scaled_dot_product = self.transformerDecoder(x, None, None,
                                                          mask=torch.zeros([1, 4096], dtype=torch.float32)) # x: [B, L, dim]
        
        # inference: encoder output + encoder output and attention weights
        # decoder input (for the last step) + self_attn with decoder inputs and encoder outputs
        # encoder hidden states + self_attn for decoder + decoder hidden states + attention weights
        # v2 is None, will be used in the next step
        x, v2, scaled_dot_product = self.transformerDecoder(x, None,
                                                             encoder_outputs=v2,
                                                             mask=torch.zeros([1, 4096], dtype=torch.float32))
        v = torch.cat((x, v), dim=-1)
        
        # inference: decoder output + attention weights
        x, v2, scaled_dot_product = self.transformerDecoder(x, None,
                                                             encoder_outputs=v2,
                                                             mask=torch.zeros([1, 4096], dtype=torch.float32))

        v = torch.cat((x, v), dim=-1)
        
        # inference: decoder output and masked input
        x, v2, scaled_dot_product = self.transformerDecoder(x, v2,
                                                             mask=torch.ones([1, 4096], dtype=torch.float32))

        v = torch.cat((x, v), dim=-1)
        
        # inference: decoder output
        x, v2, scaled_dot_product = self.transformerDecoder(x, v2,
                                                             mask=torch.zeros([1, 4096], dtype=torch.float32))

        v = torch.cat((x, v), dim=-1)

        return v
        
# Initializing the model
m = SelfAttentionNet()


class Encoder(nn.Module):
    def __init__(self,
                 embed_size=512,
                 input_dim=4096,
                 nhead=8,
                 num_encoder_layers=6,
                 dropout_rate=0.1):
        super().__init__()

        encoder_layer = TransformerEncoderLayer(d_model=embed_size, nhead=nhead,
                                              dim_feedforward=4 * embed_size)
        
        self.transformerEncoder = TransformerEncoder(encoder_layer, num_layers=num_encoder_layers)

    def forward(self, x):
        return self.transformerEncoder(x).permute(0, 2, 1) # [B, dim, L]
        
class Decoder(nn.Module):
    def __init__(self,
                 embed_size=512,
                 input_dim=4096,
                 nhead=8,
                 num_decoder_layers=6,
                 dropout_rate=0.1):
        super().__init__()

        decoder_layer = TransformerDecoderLayer(d_model=embed_size, nhead=nhead,
                                              dim_feedforward=4 * embed_size)
        
        self.transformerDecoder = TransformerDecoder(decoder_layer, num_layers=num_decoder_layers)

    def forward(self, x, v2, scaled_dot_product):
        return self.transformerDecoder(x, v \ 
1.2.9 - - - - - - - - - - - - 2018-06-04 at at at at at at at at at at at at at at at at at at at at at at at at at at at at at at at