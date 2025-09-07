

class TransformerModel(nn.Module):
    def __init__(self, d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048, dropout=0.1, activation="relu"):
        super().__init__()
        self._layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
 
    def forward(self, input):
         v  = self._layer(input)
         return v


# Initializing the model
m  = TransformerModel()

# Inputs to the model
x1 = torch.randn(300, 64, 512).to("cuda")
