
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(4, 32)
        self.key   = torch.randn(16, 32)
 
    def forward(self, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output      = attn_weight @ value   # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m = Model()
__output__    = m(torch.randn(4, 32))
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(16, 3)
 
    def forward(self, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output      = attn_weight @ value   # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
m = Model()
__output__    = m(torch.randn(4, 32))
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(16, 3)
 
    def forward(self, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output      = attn_weight @ value   # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m = Model()
__output__    = m(torch.randn(4, 32))
