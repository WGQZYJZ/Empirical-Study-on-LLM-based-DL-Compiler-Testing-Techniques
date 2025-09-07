
class Model(torch.nn.Module):
    def __init__(self, num_layers=12):
        super().__init__()
        self.num_layers = num_layers

        # Create self-attn layers
        self.transformer_attn = torch.nn.TransformerEncoderLayer(d_model=512, nhead=8)
        for _ in range(num_layers - 2):
            self.transformer_attn = torch.nn.TransformerEncoderLayer(
                d_model=512, nhead=8,
                norm_type='SyncLayerNorm', dropout=0.3)

        # Create feed-forward layer
        self.ffn = torch.nn.Linear(d_model=1024, d_model=1024, bias=True)

        # Add the layer normalization before each attention head (only used in encoder blocks)
        self.transformer_attn = torch.nn.TransformerEncoderLayer(
            d_model=512, nhead=8, norm_type='SyncLayerNorm', dropout=0.3)

        # Add two dense layers (shared weights between both self-attn and ffn layers)
        self.self_attn_layer = torch.nn.Linear(d_model=512, d_model=512, bias=True)
        self.ffn_layer = torch.nn.Linear(d_model=512, d_model=512, bias=True)

    def forward(self, x):
        # First: Perform self-attention on input data and then transform to linear space
        # Second: Apply feed-forward network (i.e., linear combination of self-attn + ffn layer)
