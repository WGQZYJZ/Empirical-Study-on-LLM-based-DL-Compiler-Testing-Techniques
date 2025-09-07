
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ x1  # dot product between the attention weight and the input
 
        return output


# Initializing the model
m = Model()


