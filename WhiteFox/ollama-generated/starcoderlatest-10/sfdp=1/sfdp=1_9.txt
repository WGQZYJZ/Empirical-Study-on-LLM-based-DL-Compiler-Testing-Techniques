
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(128, 512)
 
    def forward(self, qk_v):
        k = qk_v[0]
        v = qk_v[1]
        x = qk_v[2]
        attention = self.attention(x) # apply linear to the input tensor of size (batchsize, query_length, 36, embed_dim)
        output = torch.matmul(attention, v) # compute matmul with query: attention * value to get outputs of shape (batchsize, num_queries, embed_dim). The batchsize dim must be collapsed for further computations
