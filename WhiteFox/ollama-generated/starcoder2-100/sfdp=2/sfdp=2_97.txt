
class Model(torch.nn.Module):
    def __init__(self, d=128, d_k=None):
        super().__init__()
        self.d = d
        if not d_k:
            self.d_k  = d
        else:
            self.d_k  = d_k
        self.scale  = (self.d_k ** -0.5)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1.div(self.scale)
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5, training=True)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(64, 8, m.d_k) # query is a tensor of shape (64, 8, d/d_k). Here, 64 is batch size, and 8 is sequence length for each example in the batch
key  = torch.randn(64, 120, m.d_k) # key is a tensor of shape (64, 120, d/d_k). Here, 64 is batch size, and 120 is sequence length for each example in the batch
value  = torch.randn(m.d, 350, m.d) # value is a tensor of shape (d, 350, d/d_k). Here, 64 is batch size, and 120 is sequence length for each example in the batch


# Initializing the model
model = Model(
    d=16,  # hidden dimension of query, key, value
    d_k=None,  # hidden dimension of query, key. If not provided, set to d
)


# Inputs to the model
query = torch.randn(320, 48, 572)
key   = torch.randn(320, 96, 140)  # key is a tensor of shape (batch_size, 96, d/d_k). Here, batch size is 320, and 96 is sequence length for each example in the batch
value = torch.randn(768, 550, model.d)  # value is a tensor of shape (batch_size, 140, d/d_k). Here, batch size is 320


# Initializing the model
model  = Model(
    d=None,  # hidden dimension of query, key. If not provided, set to d
    d_k=8  # hidden dimension of query, key. Set to d/d_k for consistency between PyTorch versions
)


# Inputs to the model
query  = torch.randn(320, 48, 572) # query is a tensor of shape (batch size, 96, d/d_k). Here, batch size is 320, and 96 is sequence length for each example in the batch
key    = torch.randn(320, 48, 572) # key is a tensor of shape (batch size, 96, d/d_k). Here, batch size is 320, and 96 is sequence length for each example in the batch
value1 = torch.randn(model.d, model.d//4, 8) # value1 is a tensor of shape (batch size, query/d, d/d_k). Here, batch size is 320
value2 = torch.randn(model.d, model.d//4, 7) # value1 is a tensor of shape (batch size, query/d, d/d_k). Here, batch size is 320


# Initializing the model
model  = Model()
 
# Inputs to the model
query  = torch.randn(640, 7) # query is a tensor of shape (batch size, query/d, d/d_k). Here, batch size is 320
key    = torch.randn(512, 8) # key is a tensor of shape (batch size, 96, d/d_k). Here, batch size is 320

