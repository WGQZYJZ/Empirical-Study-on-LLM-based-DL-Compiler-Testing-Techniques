
class TransformerModel(torch.nn.Module):
    def __init__(self, d_k=64, heads=1):
        super().__init__()
        self.d_k = d_k
        self.heads = heads
 
        self.transformer_encoder  = self._make_encoder()
        self.classifier         = torch.nn.Linear(d_k, num_classes)
 
    def _make_encoder(self):
        return TransformerEncoder(
            dim=self.dim, 
            nhead=self.heads, 
            d_v=self.dim // 4, 
            dropout=0.1
        )
 
    @property
    def dim(self):
        return 64
 
    def forward(self, x1, x2, x3, x4):
        x = torch.cat((x1, x2, x3, x4), dim=-1) # Concatenate the inputs as columns
        x  = self.transformer_encoder(x)  # Generate attention weights using a transformer encoder

        x  = x.contiguous().view(-1, self.heads, self.dim)  # Expand to a vector (one per input)
        x  = self.classifier(x).contiguous()           # Combine the input-hidden state from the different layers and apply a linear transformation
        return x


# Initializing the model
model = TransformerModel()
