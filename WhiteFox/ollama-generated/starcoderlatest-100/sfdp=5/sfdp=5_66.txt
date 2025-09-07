
class Model(torch.nn.Module):
    def __init__(self, dim_1=3072, dim_2=1536):
        super().__init__()
        self.query = torch.nn.Linear(dim_1, dim_2)
        self.key = torch.nn.Linear(dim_1, dim_2)
        self.value = torch.nn.Linear(dim_2, dim_2)
 
    def forward(self, x):
        k = self.key(x)
        v = self.value(x)
        q = self.query(x)
        # Scale the query by sqrt(d_k). Then, add the scaled queries for each key-value pair to calculate the dot product.
        qk = torch.matmul(q / math.sqrt(k.size(-1)), k.transpose(-2, -1)) + attn_mask  # [bsz x nheads x seqlen x seqlen] 
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = torch.matmul(attn_weight, v)  # [bsz x nheads x seqlen x seqlen]
        return output


# Initializing the model
m = Model()

