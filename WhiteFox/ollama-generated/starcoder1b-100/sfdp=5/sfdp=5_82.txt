
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Compute the dot product of the query and key (plus an attention mask), followed by a dropout operation
        qk = self.conv1(x1) @ self.conv2(x1) / math.sqrt(self.conv1(x1).size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        v = self.conv1(x1) @ attn_weight  # Compute the dot product of the attention weights and the value
        output = v @ self.conv2(v)
        return output


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
