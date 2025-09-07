
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(1024, 64)
        self.k = torch.nn.Linear(1024, 64)
        self.v = torch.nn.Linear(1024, 64)
 
    def forward(self, query, key):
        q  = self.q(query).view(-1, 1024)  # Expand the batch to one-hot shape and then flatten to obtain a one-dimensional vector
        k  = self.k(key).view(-1, 1024)
        v  = self.v(value).view(-1, 1024)
        scale = torch.exp(qk.size(-2)/2 - query.size(-1)/2)
        return q @ k * scale  # Compute the scaled dot-product of the two vectors at a time, and finally apply the softmax to obtain an attention map


# Initializing the model
m = Model()


