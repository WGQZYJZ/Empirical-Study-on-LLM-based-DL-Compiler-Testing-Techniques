This pattern characterizes scenarios where a Transformer-based model takes as input the feature map of three different convolutional layers that share weight parameters. Each of these convolutional layers is composed by three blocks, each one using kernel size 1 in all cases. The first block contains three identical convolutions with stride=4 and padding=0; the second block has three identical convolutions with stride=2 and padding=0; and the last block has two identical convolutions with stride=1 and padding=1. In a typical use case of transformer models, each of these blocks is followed by a residual connection that adds identity mapping from intermediate features in the input tensor to the output of the corresponding convolutional layer. The intermediate features are computed as the result of successive convolutional layers.


# Model
class TransformerBlock(nn.Module):
    def __init__(self, dim, num_heads=8):
        super().__init__()
        self.conv = nn.Conv2d(dim, dim * 3, kernel_size=(1,1), stride=(1,1)) # conv layer with conv and three skip layers for feature fusion
        
        self.layer_norm1 = nn.LayerNorm((num_heads,))
        self.layer_norm2 = nn.LayerNorm(dim)
        self.layer_norm3 = nn.LayerNorm((num_heads,))
        
    def forward(self, x):

        # x (B,C,H,W), feature map after conv layer and skip layers of conv
        feat = F.relu(self.layer_norm1(x))
        #feat += self.skip_conv_1(x)
        
        feat = self.conv(feat)  # feature map in the first block
        
        feat = feat + x  # identity mapping between conv layer and skip layers for feature fusion, residual connection
        
        feat = F.relu(self.layer_norm2(feat))
        #feat += self.skip_conv_2(x)
        
        feat = feat + x  # identity mapping between conv layer and skip layers for feature fusion, residual connection
        
        feat = F.relu(self.layer_norm3(feat))
        #feat += self.skip_conv_3(x)
        
        return feat
        
class Model(nn.Module):
    def __init__(self, dim, num_heads=8):
        super().__init__()
        self.convs = nn.ModuleList([TransformerBlock(dim=dim, num_heads=num_heads)])
        
    def forward(self, x):
        
        for conv in self.convs:
            feat = conv(x)  # feature map after the transformer block
            x += feat  # add features from each convolution into output tensor

        return feat
__input__ = torch.randn((100, 3, 56, 56), device='cuda')
# Expected output shape: (100, 272, 7, 7)
print('Output tensor shape:', __output__.shape)

