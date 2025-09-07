
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.d_model = d_model
 
        self.layer_norm = torch.nn.LayerNorm(d_model)
        self.self_attn = torch.nn.MultiheadAttention(d_model, num_heads=8)
        self.pos_encoding = PositionEmbedding(1024)

        # Zero-padding so the model can take different input sizes dynamically during training (e.g., max_position_embeddings).
        # Padding values are the maximum attention values for positions that don't exist in the target language.
        self.dropout = torch.nn.Dropout(0.1)
 
    def forward(self, x):
        residual = x
 
        # Positional encoding is created to accomodate different lengths of input and outputs.
        x += self.pos_encoding[:, :x.size(-2), :x.size(-1)]  # Add position embedding (not used in training).
        
        # The input is passed through the first layer norm, followed by two convolutions:
        # 1) 4 x 4 convolution over the input to get a feature map of shape B x C x H x W where B is batch size.
        # 2) 3 x 3 convolution over the same input to get a feature map of shape D x E x F where D is hidden dimension and E is inner dimension.

        x = self.layer_norm(x)
        x = torch.nn.functional.conv2d(x, weight=self.attn_weight, bias=None)
        
        # The first output (which will be passed to the second layer norm and dropout layer) is the final embedding, so we multiply it by the same value 1:
        # If this were the first output, then it would have a shape of batch size x D x F where D is hidden dimension and F is number of features.
        x = torch.nn.functional.dropout(x * 1, p=0.15)
        
        return x


# Initializing the model
m = Model()


