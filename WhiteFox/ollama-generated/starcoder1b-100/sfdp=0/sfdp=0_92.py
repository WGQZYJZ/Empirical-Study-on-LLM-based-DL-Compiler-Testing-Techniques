
class Model(torch.nn.Module):
    def __init__(self, num_attn_heads=8, embedding_dim=64, hidden_size=512, max_position_embeddings=1024, layer_num=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(hidden_size, hidden_size)
        self.layer_num = layer_num
        # The input shape of Transformer is `num_attn_heads * embedding_dim`, so the final shape of the convolution kernel needs to be divided by the number of attention heads: conv kernel shape should become `num_attn_heads * embedding_dim / num_attn_heads`.

        assert layer_num % num_attn_heads == 0
        self.attention_layer = torch.nn.TransformerEncoderLayer(
            d_model=embedding_dim, 
            nhead=num_attn_heads, 
            dim_feedforward=hidden_size // 4,
            dropout=0.1)

    def forward(self, x1):
        query = self.conv(x1)
        x2 = torch.zeros_like(query)
        for i in range(self.layer_num):
            x3 = torch.cat([query, x2], dim=1)  # Concatenate input query and previous layer output (x2), so that `layer output shape = (batch size, num_attn_heads * embedding_dim)`

            x4, _ = self.attention_layer(
                query=x3, 
                key=x3, 
                value=x3, 
                attn_mask=None)
            x5 = torch.cat([x4, x2], dim=1)  # Concatenate input previous layer output (x4) and the new input (x2), so that `layer output shape = (batch size, num_attn_heads * embedding_dim)`

            x6, _ = self.attention_layer(
                query=x5, 
                key=x5, 
                value=x5, 
                attn_mask=None)
            x7 = torch.cat([x6, x1], dim=1)  # Concatenate the input of previous and new layer outputs (x6) and input tensor (x1), so that `layer output shape = (batch size, num_attn_heads * embedding_dim)`

            x8, _ = self.attention_layer(
                query=x7, 
                key=x7, 
                value=x7, 
                attn_mask=None)
            # If there is no need for attention in the last layer (i.e., `i == layer_num - 1`), then we will skip this update to the new input and keep `layer output shape = (batch size, embedding_dim)`
            if i != self.layer_num - 1:
                x9 = torch.cat([x8, query], dim=1)

            # Apply pointwise convolution on the newly generated input and `i == layer_num-1` corresponds to whether this is the last layer in this model or not.
            if i == self.layer_num - 1:
                x10 = self.conv(x9)
        return x8


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
