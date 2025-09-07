
class Model(torch.nn.Module):
    def __init__(self, d_k=64):
        super().__init__()
        self.w1 = torch.nn.Embedding(vocab_size, d_k)
        self.dropout = torch.nn.Dropout(p=0.25)
 
    def forward(self, x, k):
        batch_size = x.shape[0]
        input_shape = tuple([batch_size] + list(x.shape[-3:-1]))
        weight  = self.w1(x).view(*input_shape, -1).contiguous()
        output = weight @ k.transpose(-2, -1)
        return output


# Initializing the model
m = Model()


