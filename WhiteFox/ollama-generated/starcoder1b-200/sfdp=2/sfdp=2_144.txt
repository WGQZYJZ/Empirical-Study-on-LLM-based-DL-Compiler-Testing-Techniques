
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.scale_factor = 1 / math.sqrt(num_attention_heads)

    def forward(self, x, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) / self.scale_factor
        attn = qk.div(math.sqrt(self.scale_factor ** num_attention_heads))
        attn = attn.softmax(dim=-1)
        drop_attn = torch.nn.functional.dropout(attn, p=dropout_p)
        output = torch.matmul(drop_attn, value)
        return output


# Initializing the model
m = Model()


