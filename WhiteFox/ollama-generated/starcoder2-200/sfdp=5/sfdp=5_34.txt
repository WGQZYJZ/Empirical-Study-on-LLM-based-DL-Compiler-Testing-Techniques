
class Model(torch.nn.Module):
    def __init__(self, dmodel=768, nhead=12, hidden_size=3072, num_layers=12):
        super().__init__()
        self.dmodel = dmodel
        self.nhead = nhead
 
        # Transformer encoder with 3 layers and a heads of size 4 for each layer,
        # hidden representation of 512, and dropout probability of 0.1.
        encoder_layer = torch.nn.TransformerEncoderLayer(self.dmodel,
                                                        self.nhead,
                                                        hidden_size,
                                                        dim_feedforward=hidden_size)
        encoder_norm = torch.nn.LayerNorm(dmodel)
 
        self.encoder = torch.nn.TransformerEncoder(encoder_layer, 12)
 
    def forward(self):
        input = torch.randn(350, dmodel).float()
        
        # Compute the transformed representation of the input
        vq = self.encoder(input)
 
        return vq

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(768,)
__output__= m()

