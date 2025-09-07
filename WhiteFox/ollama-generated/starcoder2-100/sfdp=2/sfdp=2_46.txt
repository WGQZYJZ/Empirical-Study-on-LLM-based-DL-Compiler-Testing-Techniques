
class Model(torch.nn.Module):
    def __init__(self, scale=64**-0.5):
        super().__init__()
        self.scale = 1 / torch.tensor([scale])
 
    def forward(self, query, key, value):
        inv_scale  = self.scale * key[None] # Get the inverse scale factor. The output tensor is [batchsize x seqlen x 1 x head]
        qk  = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(inv_scale) 
        softmax_qk  = torch.nn.functional.softmax(qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.15) # Apply dropout to the softmax output
        return dropout_qk.matmul(value).mul_(self.scale)


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(2048, 3679154, 32*8) / m.scale # Get the query tensor from the original attention mechanism model. The output tensor is [batchsize x 1 x seqlen] with the shape of (batchsize, 1, seqlen).
key  = torch.randn(679154, 32*8) / m.scale # Get the key tensor from the original attention mechanism model. The output tensor is [seqlen x batchsize x 1] with the shape of (seqlen, batchsize, 1).
value  = torch.randn(679154, 32*8) / m.scale # Get the value tensor from the original attention mechanism model. The output tensor is [seqlen x batchsize x 1] with the shape of (seqlen, batchsize, 1).
output  = m(query[:, None], key[None], value[None]).squeeze()


