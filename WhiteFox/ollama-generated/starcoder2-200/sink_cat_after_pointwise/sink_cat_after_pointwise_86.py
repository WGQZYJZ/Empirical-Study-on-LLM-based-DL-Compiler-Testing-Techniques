
class Model(torch.nn.Module):
    def __init__(self, k1=0, k2=0):
        super().__init__()
        self.k1 =  torch.tensor(k1) # Some trainable parameters that are used as the concatenation keys.
        self.k2 =  torch.tensor(k2)

    def forward(self, x):
        v1  = torch.cat([x[..., :1], x[..., -1:]], dim=-1)   # Concatenate two tensors along dimension of last.
        v2  = v1.view(-1, int((v1*0).shape[-1]))           # Reshape the concatenated tensor to a vector with size = [batch_size, 4].
        v3  = torch.relu(torch.cat([v2, self.k1], dim=-1))   # Concatenate the vector and a trainable tensor.
        return v3


# Initializing the model
m  = Model()


# Inputs to the model: x1 and x2 are of shape [N]
x1  = torch.randn(8, )    # N is the number of observations/examples in each batch.
x2  = torch.randn(40, 5)  # 5 is the input size.
__output__  = m(torch.cat([x1[:, None], x2, x1[..., None]], dim=-1))

