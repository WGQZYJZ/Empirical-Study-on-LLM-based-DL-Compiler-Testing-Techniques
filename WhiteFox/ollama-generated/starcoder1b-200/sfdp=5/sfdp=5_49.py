
class Model(torch.nn.Module):
    def __init__(self, args):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()
        self.attn  = MultiHeadedAttention(args.hidden_size, args.num_heads)
        self.dense1 = DenseBlock(args.hidden_size, args.hidden_size, self_attention=True)
        self.dense2 = DenseBlock(args.hidden_size * 4, args.hidden_size, self_attention=True)

    def forward(self, x1, x2):
        q  = torch.cat((x1, x2), dim=-1)
        k  = self.attn(q, x1, x2, True)[0]
        v  = self.attn(q, x2, x1, True)[0]

        o1 = self.dense1(self.dropout(k))
        o2 = self.dense2(self.dropout(v))
        
        