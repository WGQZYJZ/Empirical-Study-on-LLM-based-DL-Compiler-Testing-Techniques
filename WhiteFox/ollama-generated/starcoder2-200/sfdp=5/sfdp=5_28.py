
class TransformerModel(torch.nn.Module):
    def __init__(self, embedding_dim=512, nhead=8, num_layers=6, dim_feedforward=2048, dropout=0.1, activation="relu"):
        super().__init__()
        self.encoder_layer = torch.nn.TransformerEncoderLayer(embedding_dim, nhead, dim_feedforward, dropout)
        self.encoder  = torch.nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
 
    def forward(self, src):
        attn_mask  = (src == 0).unsqueeze(1).expand(-1, -1, -1) # Compute the attention mask for the source sequence
        output  = self.encoder(src, src_key_padding_mask=attn_mask)  # Encode the source sequence using a transformer encoder layer with the attention mask
        return output


# Initializing the model