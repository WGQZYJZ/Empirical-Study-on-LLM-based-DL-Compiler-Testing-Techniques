
class MultiheadAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc_q = torch.nn.Linear(dim, dim) # Query (Kx1024x7x7)
        self.fc_k = torch.nn.Linear(dim, dim) # Key (Mx512x3x3)
        self.fc_v = torch.nn.Linear(dim, dim) # Value (Hx64x8x8)
        self.fc_o = torch.nn.Linear(dim*2, dim) # Output (Nx128x7x7)
 
    def forward(self, query, key, value): 
        nq, nx = query.shape[0], key.shape[0]
 
        batch_size = query.shape[0]
        q = self.fc_q(query).view(-1, nx, 1) # (NxK)
        k = self.fc_k(key).view(-1, nq, 1) # (KxN)
        v = self.fc_v(value).view(-1, nx, batch_size) # (NxV)
        dots = torch.matmul(q, k) / math.sqrt(nx * key.shape[-1])
 
        attention_weights = torch.softmax(dots, dim=-1) 
        output = torch.matmul(attention_weights, v).view(-1, nx, batch_size) # (NxV)
        x = self.fc_o(torch.cat((query.squeeze(), key.squeeze()), dim=1)) # (NxK+N) -> (NxD)
 
        return x, output


class Model(torch.nn.Module):
    def __init__(self, nx):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # Cx64x7x7 -> (CxHxW), nx = 1024
        self.multihead_attention = MultiheadAttention(nx)
 
    def forward(self, x1): 
        v = self.conv(x1) # HxW xnx3
        attention_output, _ = self.multihead_attention(v, v, v)  # NxD xH xW
        return v + attention_output


# Initializing the model
m = Model(1024)


