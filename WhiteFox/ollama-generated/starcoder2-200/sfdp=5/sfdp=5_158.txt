
class TransformerModel(torch.nn.Module):
    def __init__(self, dim=768, num_layers=12, heads=12):
        super().__init__()

        self.encoder = torch.nn.TransformerEncoderLayer(dim, 
                                                         norm='layernorm',
                                                         dropout=0.5)
        self.decoder = torch.nn.TransformerDecoderLayer(dim, 
                                                        norm='layernorm', 
                                                        dropout=0.1)

    def forward(self, src):
        src = src.permute(0,2,3,1).reshape(-1,src.shape[-2],768) # [N,H*W,Dim] -> [N*H*W, Dim]
        enc_output = self.encoder(src)
        dec_output  = self.decoder(enc_output)
        dec_output  = dec_output.reshape(-1, src.shape[-2], -1) # [N*H*W, Dim, 768]->[N, H, W]
        dec_output  = dec_output.permute(0,3,1,2).reshape(*src.shape) # [N, 768, H, W] -> [N, H, W, 768]
        return dec_output

# Initializing the model
model = TransformerModel()

