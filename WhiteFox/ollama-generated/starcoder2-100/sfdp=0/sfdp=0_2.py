
class Model(torch.nn.Module):
    def __init__(self, inv_scale):
        super().__init__()
        self.inv_scale = inv_scale
 
    def forward(self, x1, x2):
        t0  = torch.matmul(x1, x2.transpose(-2, -1)) / self.inv_scale 
        t1  = t0.softmax(dim=-1) 
        return t1.matmul(x2)

# Initializing the model
m  = Model(4.)


# Inputs to the model
x1  = torch.randn(8, 64)   # shape (batch_size x embedding_dim) or (batch_size x seq_len x embedding_dim). batch_size or sequence length should be the same as the previous input.
x2  = torch.randn(8, 64)


__output__  = m(x1, x2)
