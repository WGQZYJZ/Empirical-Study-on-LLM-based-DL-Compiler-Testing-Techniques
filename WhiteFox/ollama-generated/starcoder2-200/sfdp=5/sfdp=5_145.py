
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model=512, d_ffn=2048, num_heads=8, dropout_p = 0.1):
        super().__init__()

        self.encoder_layer = torch.nn.TransformerEncoderLayer(d_model, nhead=num_heads)
        self.attn_mask = torch.zeros(len(inputs), len(inputs))

        for i in range(len(inputs)):
            self.attn_mask[i][i] = 1


    def forward(self, inputs):
        mask = (self.attn_mask == 0).unsqueeze(-2) # Create a mask where each row is the attention mask
        enc = self.encoder_layer(inputs, mask=mask) # Apply the encoder layer to the inputs
        return enc


# Initializing the model
model = TransformerModel()

# Inputs to the model
inputs = torch.rand((512,))  # Create a random tensor of shape (512,) to be used as input for the model

