
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attn = ScaledDotProdAttention()
 
    def forward(self, x1):
        # query, key and value are the input tensors of the model's encoder
        query = self.conv(x1)
        value = torch.randn_like(query)
        attention_weights  = self.attn(query=query,
                                          key=value,
                                          value=value,
                                          scale_factor=torch.sqrt(3))
        # output is the output of the model's encoder by multiplying
        # the attention weights and the value tensor
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m  = Model()


