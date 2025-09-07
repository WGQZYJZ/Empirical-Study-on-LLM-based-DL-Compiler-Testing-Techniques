
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers=6, mlp_dim=2048):
        super().__init__()
        self.layer = torch.nn.TransformerEncoderLayer(d_model, nhead, mlp_dim)
        self.position_embeddings = torch.nn.Embedding(max_len, d_model)
 
    def forward(self, x1, x2, attn_mask):
        # Get the position embedding for each input token by using the positional encodings in
        # PositionalEncodingLayer
        positions = torch.arange(max_len).unsqueeze(0).expand(attn_mask.shape[0], 1)
        embed = self.position_embeddings(positions)
        
        attn = x1 @ x2.transpose(-1, -2) / math.sqrt(x1.size(-1))
        
        # Use the input embeddings and the positional encodings to get the attention weights for each
        # token in the sequence (one batch of inputs)
        attn_weight = torch.softmax(attn * attn_mask, dim=-1) 
        
        # Use the dropout mask to create the output using the scaled dot product
        output = self.layer[-1](attn_weight, embed, src_key_padding_mask=attn_mask).transpose(-2, -1)
        
        return output


# Initializing the model
m = Model(8, 4)


