
class Model(torch.nn.Module):
    def __init__(self, embed_size=256):
        super().__init__()
        self.linear1 = torch.nn.Linear(embed_size, 256)
        self.linear2 = torch.nn.Linear(256, 256)
 
    def forward(self, x1, x2, x3, x4):
        # Use the input to construct an intermediate hidden representation
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
 
        # Compute a dot product between the query and key vectors
        kq = torch.matmul(v1, x2.transpose(-2, -1)) / 32
        scaled_qk = kq.div(math.sqrt(256))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        # Compute the value vectors from input to key and key to query
        v3 = torch.matmul(x2, dropout_qk) / 4
        v4 = torch.matmul(dropout_qk, x3.transpose(-2, -1)) / 8
        output = v3 + v4
 
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 50, 256)
x2 = torch.randn(1, 256)
x3 = torch.randn(1, 256)
x4 = torch.randn(1, 256)
