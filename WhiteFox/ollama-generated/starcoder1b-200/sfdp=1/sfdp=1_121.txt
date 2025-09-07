
class Model(torch.nn.Module):
    def __init__(self, num_layers=4):
        super().__init__()
        self.enc = torch.nn.TransformerEncoder(self.src_embedding, src_encoder)
        self.dec = torch.nn.TransformerDecoder(self.tgt_embedding, tgt_decoder)
 
    def forward(self, x1):
        return self.dec(x1, encoder_input=x1)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
