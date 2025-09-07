
class Model(torch.nn.Module):
    def __init__(self, dim_model, dim_key=64, dim_value=64, dim_head=256, dim_inner=4096, dropout_p=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(dim_model, dim_inner, kernel_size=1)
        self.layernorm1 = LayerNorm(dim_inner)
        self.layernorm2 = LayerNorm(dim_inner)
        self.layernorm3 = LayerNorm(dim_inner)
        self.attn = TransformerEncoderLayer(dim_head, dim_inner, dropout_p=dropout_p)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + 1  # Add a constant of 1 to the output of convolution
        v3 = v1 * 0.7071067811865476 + 1  # Add a constant of 1 to the output of convolution
        v4 = torch.erf(v3)
        v5 = v4 * (2 / dim_key ** 0.5)  # Calculate the value of scaled dot product
        v6 = self.attn(v5, x1).transpose(-2, -1)  # Apply the encoder layer to calculate the output of attention module
        v7 = self.layernorm1(torch.cat([v2, v6], dim=-1))
        v8 = self.layernorm2(torch.cat([v7, v3], dim=-1))
        v9 = torch.nn.functional.dropout(v8, p=dropout_p)  # Apply dropout to the output of attention module
        v10 = self.layernorm3(torch.cat([v9, v2], dim=-1))
        return v10


# Initializing the model
m = Model(dim_model=64)


