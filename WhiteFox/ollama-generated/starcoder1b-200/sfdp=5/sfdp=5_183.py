
class Model(torch.nn.Module):
    def __init__(self, num_layers, d_model=512, heads=8, num_attention_heads=4, d_k=64, dropout=0.2, attn_dropout=0.0, max_position_embeddings=512):
        super().__init__()
        self.num_layers = num_layers
        self.d_model = d_model
        self.heads = heads
        self.num_attention_heads = num_attention_heads
        self.d_k = d_k
        self.dropout = dropout
        self.attn_dropout = attn_dropout
        self.scale = 1 / math.sqrt(self.d_k)
        self.position_embedding = torch.zeros((max_position_embeddings, heads, d_model))
        self.decoder = PositionalEncodingLayer(num_layers=num_layers, max_position_embeddings=max_position_embeddings, dropout=dropout, scale=scale)

    def forward(self, input, target):
        bsz = input.shape[0]
        # Compute the embeddings of the input tensor
        x1  = self.decoder(input)

        # The output is the dot product of the position-wise attention weights
        # and the value vector at each time step (encoder layers). We normalize by dividing through sqrt(d_k) to avoid numerical issues.
        output = torch.matmul(x1, target) / self.scale

        if not self.training:
            return output
        # We add the padding token to the input tensor and compute the
        # scaled dot product of the query and value at each time step (encoder layers).
        x2 = input[:, :-1] + target[:, 1:]  # [B, T+1, d_k]
        kq = torch.matmul(x2, x1) / math.sqrt(self.d_k)
        kq *= self.scale

        # We compute the attention weights with the scaled dot product, using an attention mask to avoid the division by zero.
        attn_mask = (torch.triu(torch.ones(qk.shape[0], kq.shape[1]), diagonal=1).to(device) != 0).type_as(kq) # [B, T+1, T+1]

        # We apply dropout to the output and the attention mask
        attn_weight = torch.softmax(qk * self.attn_dropout + self.attn_dropout, dim=-1) # [B, T, T]
        attn_weight = torch.dropout(attn_weight, self.dropout, True)

        # We compute the output and the attention weights at the same time by
        # combining the two steps in a single forward pass.
        output = torch.matmul(attn_weight, x1)  # [B, T, d_model]
        output = output + target * self.scale

        return output


# Initializing the model
m = Model(num_layers=3)


# Inputs to the model
input = torch.randn((10, 512, 64, 64))
target = torch.randn((10, 512, 64, 64))
