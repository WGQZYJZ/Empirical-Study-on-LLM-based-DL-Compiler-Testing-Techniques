
class Model(torch.nn.Module):
    def __init__(self, query_channels, key_channels, attn_head_num=16, attn_emb_dim=64):
        super().__init__()
        self.query_conv  = torch.nn.Conv2d(query_channels, query_channels, 1)
        self.key_conv     = torch.nn.Conv2d(key_channels, key_channels, 1)
        self.attn_head    = []
        for _ in range(attn_head_num):
            self.attn_head.append(torch.nn.Linear(query_channels, key_channels))
            # Create a linear layer with query_conv.weight and key_conv.weight initialized as normal distribution
            nn.init.xavier_normal_(self.attn_head[-1].weight)

        self.value_conv   = torch.nn.Conv2d(query_channels, attn_emb_dim, 1)
        # Create a conv layer with the same parameters of self.value_conv and initialized as normal distribution

    def forward(self, x1, x2):
        query  = self.query_conv(x1)
        key     = self.key_conv(x2)
        attn_mask = torch.eye(key.shape[-1]).unsqueeze(-2).expand(-1, -1, x1.size(-2), x1.size(-1))
        # Add the attention mask to the result of query and key
        attn_weights  = torch.softmax(query @ key / math.sqrt(key.size(-1)), dim=-1)
        attn_weights  = torch.dropout(attn_weights, dropout_p, True)
        value = self.value_conv(x2)
        # Compute the dot product of the result of query and key, and scale it to prevent the overflow
        attn_weights @ value  # Apply softmax to the result

        output = []
        for i in range(attn_head_num):
            output.append(self.attn_head[i](attn_weights[i]))
            # Create a linear layer with query_conv.weight and key_conv.weight initialized as normal distribution
        return output


# Initializing the model
m = Model(query_channels=3, key_channels=8, attn_head_num=4, attn_emb_dim=64)
