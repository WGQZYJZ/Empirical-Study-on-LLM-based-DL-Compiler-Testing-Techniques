
class MultiHeadAttentionBlock(torch.nn.Module):
    def __init__(self, in_dim, out_dim, num_heads=8, dropout=0., batchnorm=True):
        super().__init__()
        self.batchnorm = batchnorm
        if self.batchnorm:
            self.layer1 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=1),
                torch.nn.BatchNorm2d(in_dim // num_heads),
                torch.nn.ReLU(),
                torch.nn.Conv2d(in_dim // num_heads, out_dim, 1))
            self.layer2 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=3),
                torch.nn.BatchNorm2d(in_dim // num_heads),
                torch.nn.ReLU(),
                torch.nn.Conv2d(in_dim // num_heads, out_dim, 1))
        else:
            self.layer1 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=1),
                torch.nn.ReLU(),
                torch.nn.Conv2d(in_dim // num_heads, out_dim, 1))
            self.layer2 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=3),
                torch.nn.ReLU(),
                torch.nn.Conv2d(in_dim // num_heads, out_dim, 1))

        self.norm = torch.nn.LayerNorm([out_dim, in_dim])
        self.dropout = torch.nn.Dropout(p=dropout)

    def forward(self, x):
        x1 = x
        x2 = self.layer1(x1) + self.layer2(x1)
        if self.batchnorm:
            x3 = self.norm(x2) * 1
        else:
            x3 = self.norm(x2)
        x4 = torch.mean(x3, dim=[2, 3], keepdim=False)
        x5 = self.dropout(x4)
        x6 = x3 - x5 + x1
        return x6


class MultiHeadAttentionLayer(torch.nn.Module):
    def __init__(self, in_dim, out_dim, num_heads=8, dropout=0., batchnorm=True):
        super().__init__()
        self.attention = MultiHeadAttentionBlock(in_dim, out_dim, num_heads, dropout, batchnorm)

    def forward(self, x, key, query):
        attn = self.attention(x) # Attention module
        qk = torch.einsum('bhd,bhef->bhdf', (query, attn))  # Scale and sum the attention weights

        return qk


class TransformerLayerBlock(torch.nn.Module):
    def __init__(self, in_dim, out_dim, num_heads=8, dropout=0., batchnorm=True):
        super().__init__()
        self.batchnorm = batchnorm
        if self.batchnorm:
            self.layer1 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=3),
                torch.nn.BatchNorm2d(in_dim // num_heads),
                torch.nn.ReLU(),
                MultiHeadAttentionLayer(in_dim, out_dim, num_heads, dropout))
            self.layer2 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=3),
                torch.nn.BatchNorm2d(in_dim // num_heads),
                torch.nn.ReLU(),
                MultiHeadAttentionLayer(in_dim, out_dim, num_heads, dropout))
        else:
            self.layer1 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=3),
                torch.nn.ReLU(),
                MultiHeadAttentionLayer(in_dim, out_dim, num_heads, dropout))
            self.layer2 = torch.nn.Sequential(
                torch.nn.Conv2d(in_dim, in_dim // num_heads, kernel_size=3),
                torch.nn.ReLU(),
                MultiHeadAttentionLayer(in_dim, out_dim, num_heads, dropout))

        self.norm = torch.nn.LayerNorm([out_dim, in_dim])
        self.dropout = torch.nn.Dropout(p=dropout)

    def forward(self, x):
        if self.batchnorm:
            x1 = self.layer1(x) * 1 # The first layer applies batchnorm to the input tensor and multiplies it by 1
        else:
            x1 = self.layer1(x)

        if self.batchnorm:
            x2 = self.layer2(x1) * 1 # The second layer applies batchnorm to the output of the first layer, and multiplies it by 1
        else:
            x2 = self.layer2(x1)

        return x2 + x


class TransformerLayer(torch.nn.Module):
    def __init__(self,
                # This is a note! A new one!!!",!,!,!")]
    if_type, 
    n_taps,
    stride,
    num_channels // 4,
    (num_channels % 4 == 0 ? 1 : 0),
    q,
};


#ifdef __cplusplus
}
#endif /* __cplusplus */


