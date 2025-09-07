
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead):
        super().__init__()
        self.layer  = torch.nn.TransformerEncoderLayer(d_model, nhead)
 
    def forward(self, x1, attention_mask=None):
        # Initialize transformer encoder
        encoder_out  = x1
        # Encode as long as there are remaining words in the sequence
        while True:
            h = self.layer(encoder_out, attention_mask)  # Run a single layer through the encoder
            encoder_out = h.last_hidden_state

# Initializing the model
m = Model(512, 8)


