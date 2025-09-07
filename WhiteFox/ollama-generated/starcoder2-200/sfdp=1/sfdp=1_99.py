
class Model(torch.nn.Module):
    def __init__(self, scale=1.0, dropout_p=0.3):
        super().__init__()

        self.scale = torch.tensor(float(scale))
        self.dropout  = torch.nn.Dropout(p=dropout_p)

        self.q = torch.nn.Linear(768, 256)
        self.k = torch.nn.Linear(768, 1024) # the number of channels is changed for this model
        self.v = torch.nn.Linear(768, 1024)

        self.attn = torch.nn.MultiheadAttention(embed_dim=3072, num_heads=512)

    def forward(self, qk):
        key  = self.q(qk).transpose(-2,-1).reshape(batchsize, sequence, 3072) # 3072 is the new number of channels 
        value = torch.nn.functional.normalize(qk)
        attention_output, _ = self.attn(query=self.k(key), key=self.v(value))
        return self.dropout(torch.nn.functional.normalize(attention_output).reshape(batchsize, sequence, 768))


# Initializing the model
m  = Model()
__output___ = m(x1)

