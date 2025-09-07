
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=128, num_heads=4, dropout_p=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=4, embedding_dim=embedding_dim)
        self.norm_layer_kv = torch.nn.LayerNorm(embedding_dim*2)
        self.ffn_layer_kv = torch.nn.Linear(in_features=128, out_features=3072) # Number of parameters in ffn_layer: 128+3072-5936 = 3104

    def forward(self, query, key):
        attn_output, attn_weight = self.attn(query=query, key=key, value=key) # Apply multihead attention to compute the output and attention weights

        x_norm = torch.nn.functional.layer_norm(attn_output + query, axis=-1)

        ffn_output = torch.nn.functional.linear(x_norm, self.ffn_layer_kv)
        ff_input = torch.cat((x_norm, ffn_output), dim=-1) # Add the attention output and the value to create an input for a feed forward network

        ffn_output2 = torch.nn.functional.relu(torch.nn.functional.linear(ff_input, 3072))
        x_norm_2 = self.norm_layer_kv(x_norm + torch.nn.functional.layer_norm(attn_output + ffn_output2, axis=-1))

        attn_output_2, _ = self.attn(query=x_norm_2, key=key, value=key) # Apply multihead attention again to compute the output and attention weights
        return x_norm_2, attn_output_2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # shape (batch size, number of channels in each image, height of an image, width of an image)
__output_kv__, __output_2__ = m(x1, x1)

