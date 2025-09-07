
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4


# Initializing the model
m  = Model()
scale_factor = random.uniform(-0.99, 0.5)
dropout_p    = random.randint(1, 20) / 10
 
# Inputs to the model
query        = torch.randn(64, 32, 8, 8).cuda()
key          = torch.randn(64, 32, 8, 8).transpose(-2, -1).cuda()


__output__  = m(query, key)
