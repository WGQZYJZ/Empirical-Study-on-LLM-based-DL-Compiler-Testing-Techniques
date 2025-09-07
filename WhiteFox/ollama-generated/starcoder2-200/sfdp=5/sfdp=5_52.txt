
class Model(torch.nn.Module):
    def __init__(self, dmodel=768, vocab_size=2104935):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size + 4, dmodel)
        self.pos_encoder = PositionalEncoding(dmodel, dropout=True)
        self.layernorm1 = torch.nn.LayerNorm([0])
        self.layernorm2 = torch.nn.LayerNorm([1])
        self.attn1 = MultiHeadAttention(dmodel)

    def forward(self, input):
        emb  = self.embedding(input).float()
        pos_emb  = self.pos_encoder(emb)
        out1  = self.layernorm1(pos_emb) # Layer norm 1
        attn1 = self.attn1(out1, out1, out1)
        attn2 = self.layernorm2(attn1 + out1)  # Layer norm 2
        return attn2

m = Model()
x1  = torch.randint(0, m.embedding.weight.shape[0], (768,))


__output__  = m(x1)
