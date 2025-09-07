
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, num_layers, dropout_p):
        super().__init__()
        self.num_layers = num_layers
        self.embed_dim = embed_dim
        self.dropout_p = dropout_p
        # Input embedding layer
        self.input_embedding = torch.nn.Linear(in_features=1, out_features=8)
        
        # Output embedding layer
        self.output_embedding = torch.nn.Linear(in_features=16, out_features=4)
        
        # Transformer encoder layer block
        self.layernorm1 = torch.nn.LayerNorm((num_heads * embed_dim), eps=1e-12)
        self.feed_forward_net = SelfAttentionWithPositionEncodingBlock(embed_dim=embed_dim, num_heads=num_heads, dropout_p=dropout_p)
        
        # Multihead attention layer
        self.self_attention_layer = torch.nn.MultiheadAttention(embed_dim=embed_dim, num_heads=num_heads, dropout_p=dropout_p)
        
        # Position encoding block (positionwise)
        self.feedforward_block = FeedForwardBlock(embed_dim=embed_dim, num_layers=num_layers)
        
        # Output layer
        self.output_layer = torch.nn.Linear(in_features=4096, out_features=4)
        
        # Final output normalization layer
        self.final_layernorm = torch.nn.LayerNorm((4 * embed_dim), eps=1e-12)
    
    def forward(self, x1):
        input_tensor = self.input_embedding(x1)
        
        output = F.gelu(self.output_embedding(input_tensor))
        
        # Transformer encoder layer block
        for layer in range(self.num_layers):
            output = self.feed_forward_net(
                query=output, 
                key=output, 
                value=output, 
            )

        query = output[:,0:8,:]
        key   = output[:,:,8:16]
        value = output[:,:,16:24]
        
        # Multihead attention layer
        q, k, v = self.self_attention_layer(
            query=query,
            key=key,
            value=value, 
        )
        
        # Layer norm block
        output = self.layernorm1(output + torch.einsum('b c h w -> b (c h) w', q))
        
        # Position encoding layer (positionwise)
        output = F.gelu(self.feedforward_block(output))
        
        # Multihead attention layer (self attention mechanism)
        query = torch.nn.functional.interpolate(query, size=(16,8), mode='trilinear')
        key   = torch.nn.functional.interpolate(key,   size=(16,8), mode='trilinear')
        value = torch.nn.functional.interpolate(value, size=(16,8), mode='trilinear')
        
        qk  = torch.einsum('b s m d -> (b h) n d', query) @ k.transpose(-2,-1).unsqueeze(-1)
        scaled_qk = F.softmax(qk, dim=-1) * scale_factor # Scale the dot product by a factor
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        output   = torch.einsum('b (b h) n d -> b s m', dropout_qk, v).squeeze(-1)
        
        output = F.gelu(output + query)
        
        # Layer norm block (final)
        output = self.final_layernorm(output + input_tensor)
        
        # Output layer
        return self.output_layer(output)


# Initializing the model and parameters
m = Model(embed_dim=4, num_heads=8, num_layers=6, dropout_p=0.1)


# Inputs to the model
x1 = torch.randn(20, 1, 16, 8)
