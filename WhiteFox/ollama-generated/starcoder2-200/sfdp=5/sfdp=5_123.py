
class TransformerModel(torch.nn.Module):
    def __init__(self, ntoken, d_model=512, nhead=8, dff=2048):
        super().__init__()
 
        self.pos_encoding = PositionalEncoding(d_model)

        self.encoder = torch.nn.Sequential(
            torch.nn.Dropout(),  # Apply dropout to the input
            TransformerEncoderLayer(d_model),  # Compute the dot product of the query and key, and scale it
        )
 
        self.decoder = torch.nn.Sequential(
            torch.nn.Dropout(), 
            DecoderLayer(d_model)  
        )
 
    def forward(self, src):
        output1  = self.pos_encoding(src) + self.encoder() # compute the dot product of the query and key, and scale it
        return output2
 
m  = TransformerModel()


# Initializing the model
x1  = torch.randn(4096)
__output__  = m(x1)

