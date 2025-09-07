
class Attention(torch.nn.Module):
    def __init__(self, n_head=128, d_model=512):
        super().__init__()
 
        self.qkv = torch.nn.Linear(d_model, n_head * 3, bias=False)
 
    def forward(self, x):
        batch_size, n_head, _dim = x.shape
 
        q, k, v = [x.reshape(-1, n_head, _dim).permute(0, 2, 1)] * 3
        query, key, value = self._scaled_dot_product_attention(q, k, v)
        attention = self._dropout(query, p=0.5)
 
        return attention
 
    def _scaled_dot_product_attention(self, q, k, v):
        # q = (batch_size x n_head x len x d_model), 
        # k = (batch_size x n_head x len x d_model), 
        # and v = (batch_size x n_head x len x d_model)
        batch_size, len_q, _dim  = q.shape
        
        attention = torch.matmul(q, torch.transpose(k, -1, -2)) / math.sqrt(d_k)
 
        return query, key, value
 
    def _dropout(self, x, p=0.1):
        # Dropout is applied to a tensor with probability 1-p

        return x * (torch.rand(*x.shape, device=device) < p).float()
 
    def _activation(self, x):
        return torch.relu(x)
 
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.d_model = 512
        self.n_head = 64
 
        self.attention = Attention(self.n_head, self.d_model)
 
    def forward(self, x):
 
        batch_size = x.shape[0]
        len_q = x.shape[-1]
 
        q = torch.reshape(x[:, :, -len_q:, :], (batch_size, 64, self.n_head * self.d_model))
        v = torch.reshape(x[:, :, :len_q, :], (batch_size, 64, self.n_head * self.d_model))
 
        attention = self.attention(q)
 
        x = torch.matmul(attention, v)
 
        return x
 
 
# Initializing the model
m = Model()

