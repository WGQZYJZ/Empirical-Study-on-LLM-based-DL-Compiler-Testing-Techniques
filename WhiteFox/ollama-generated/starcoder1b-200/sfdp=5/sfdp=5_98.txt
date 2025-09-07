
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()
 
    def forward(self, x1, x2):
        z1 = self.encoder(x1)  # Encode the input x1
        y1 = self.decoder(z1)  # Decode the encoded input
        return y1


# Initializing the model
m = Model()


# Inputs to the model
z1 = torch.randn(3, 512, dtype=torch.float, device='cuda')
z2 = torch.randn(1024, 128, dtype=torch.float, device='cuda')
