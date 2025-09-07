
class Transformer_Model(torch.nn.Module):
    def __init__(self, input_dim=3, output_dim=256, hidden_dim=1024, num_heads=8):
        super().__init__()
        self.encoder = torch.nn.TransformerEncoder(
            torch.nn.TransformerEncoderLayer(
                input_dim, 
                output_dim, 
                num_heads,
                activation="relu"
            ),
            3)
 
    def forward(self, x1):
        attn_output = self.encoder(x1)
        return attn_output

# Initializing the model
m = Transformer_Model()


