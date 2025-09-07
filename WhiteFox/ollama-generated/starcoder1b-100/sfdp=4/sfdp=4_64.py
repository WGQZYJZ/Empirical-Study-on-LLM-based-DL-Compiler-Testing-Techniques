
class Model(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, num_attn_heads=4, max_seq_length=50, embed_dim=768):
        super().__init__()

        self.embed_dim = embed_dim
        self.pos_embedding  = torch.nn.Embedding(max_seq_length + 1, embed_dim)
        self.ffn = torch.nn.Sequential(
            torch.nn.Linear(embed_dim * 2, d_model),
            torch.nn.GELU(),
            torch.nn.Dropout(0.1),
            torch.nn.Linear(d_model, d_model),
            torch.nn.Dropout(0.1)
        )

        self.layers = torch.nn.ModuleList()
        self.layers.append(torch.nn.TransformerEncoderLayer(d_model, nhead))
        for i in range(2):
            self.layers.append(torch.nn.TransformerEncoderLayer(d_model, nhead))
        self.layers.append(torch.nn.TransformerEncoderLayer(d_model, nhead))

        self.final = torch.nn.Linear(d_model * 4, embed_dim)
 
    def forward(self, x1, x2, attention_mask):
        
        # The first and second hidden states of the model are initialized with the positional encodings from the input data
        self.pos_embedding.weight.data = torch.nn.init.xavier_normal_(self.pos_embedding.weight.data)
        self.ffn(x1)
        x2 = self.ffn(x2)

        for i, layer in enumerate(self.layers):
            if i > 0:
                # Compute the attention weights over all the time steps. We use the mask to decide whether we take the weighted average of the value or not.

                qkv = layer.conv_self.weight @ x1[:, None] + layer.self_attn(x1, x1)  # (batch_size, seq_length, embed_dim)
                k = qkv[0]  # (batch_size, seq_length, embed_dim)

                v = qkv[1]  # (batch_size, seq_length, embed_dim)
                attn_mask = attention_mask[:, None] * (1.0 - attention_mask[:, :, :].view(-1, 1).expand_as(v)) # (batch_size, seq_length, seq_length)

                x = k @ v.transpose(-2, -1)  # (batch_size, embed_dim, seq_length)
                attn_weights = layer.self_attn.softmax(x, dim=-1) # (batch_size, seq_length, seq_length)

                if i < len(self.layers) - 1:
                    x = torch.cat((x, attn_weights), dim=1)

            x = layer.conv_out(torch.cat((x, self.pos_embedding[:, :, None]), dim=-1)) # (batch_size, embed_dim * 2, seq_length)

        return self.final(x2)


# Initializing the model
m = Model()


