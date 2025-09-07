
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, 3 * d_k)
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x1, x2):
        qk = self.qkv(x1).chunk(3, dim=-1)
        q, k, v = map(lambda t: t.contiguous().view(-1, d_k), (qk[0], qk[1], qk[2]))
 
        attn = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and the key
        attn = attn / math.sqrt(d_k)  # Scale the dot product by the inverse square root of the dimension of the key
        attn = self.dropout(torch.nn.functional.softmax(attn, dim=-1))  # Apply dropout to the softmax output
 
        return torch.matmul(attn, v)


# Initializing the model
m = Model()


