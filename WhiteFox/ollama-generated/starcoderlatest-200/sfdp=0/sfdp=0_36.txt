
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.chanel_in = nn.Conv2d(dim, dim//8, 1)
        self.chanel_out = nn.Conv2d(dim//8, dim, 1)
 
        self.fc = nn.Linear(dim, dim)
 
    def forward(self, x):
        x = F.relu(self.chanel_in(x))
        x = F.relu(self.chanel_out(x))
        x = x.view(-1, x.shape[1])
        x = self.fc(x)
 
        return x
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        dim = 512
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=dim, nhead=8)
 
        self.decoder_layer = nn.TransformerDecoderLayer(d_model=dim, nhead=8)
        self.attention = Attention(dim)
 
    def forward(self, src, trg):
        # Forward pass
        enc_src = self.encoder_layer(src, src, src)  # (batch_size, src_len, dim)
        dec_trg = self.decoder_layer(enc_src, src, src)  # (batch_size, trg_len, dim)
 
        attention_weights = self.attention(dec_trg).unsqueeze(1)  # (batch_size, 1, trg_len, dim)
        # dec_trg = torch.bmm(attention_weights, value)  # (batch_size, trg_len, dim)
 
        # return attention_weights, dec_trg

        # Forward pass + backprop
        enc_src = self.encoder_layer(enc_src, src, src)  # (batch_size, src_len, dim)
        # dec_trg = self.decoder_layer(dec_trg, src, src)  # (batch_size, trg_len, dim)
 
        return enc_src
 
    def generate_with_attention(self, max_len=10):
        x = torch.randn(1, 3, 64, 64)
        enc_src = self.encoder_layer(x, src, src)
 
        trg = torch.ones(max_len, 8).to('cuda') * -100

        for i in range(max_len):
            attention_weights = self.attention(trg).unsqueeze(1)
            # dec_trg = torch.bmm(attention_weights, value)
            trg = F.log_softmax(trg.view(-1, self.vocab_size), dim=-1)
            probas = trg[0]
            probas = F.softmax(probas, dim=-1).unsqueeze(-1)
            # print(trg.shape)

            enc_src = (enc_src + x*probas).detach()
            attention_weights = F.softmax(attention_weights.squeeze(1), dim=-1)
            probas = torch.bmm(attention_weights, enc_src)
            sampled = torch.multinomial(probas, num_samples=1) # (batch_size, 8)
            x = self.embedding(sampled).unsqueeze(0)

        return trg


# Initializing the model
m = Model()
x = torch.randn(1, 3, 64, 64)
 
y = m.forward(x, None)
z = m.generate_with_attention()
assert list(y.shape) == [1, 8]
assert list(z.shape) == [1, 8]

