
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1, num_layers=6):
        super().__init__()
        self.transformer = torch.nn.TransformerEncoderLayer(d_model=d_model,
                                                              nhead=num_heads, 
                                                              dim_feedforward=4*d_model, 
                                                              dropout=dropout)
        self.linear = torch.nn.Linear(d_model, d_model)

    def forward(self, x):
        encoded = self.transformer(x)
        out1 = torch.relu(self.linear(encoded)) 
        return out1


# Initializing the model
m = TransformerModel(32, 8)

# Inputs to the model
x = torch.randn(4, 32, 32)
