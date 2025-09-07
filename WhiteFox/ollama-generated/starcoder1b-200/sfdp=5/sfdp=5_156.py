
class Model(torch.nn.Module):
    def __init__(self, dim_q, dim_k, dim_v):
        super().__init__()
        self.query  = torch.nn.Parameter(
            torch.FloatTensor(dim_q, dim_k).normal_() * math.sqrt(dim_k))  # Use the normal distribution to initialize the query layer parameters
        self.key    = torch.nn.Parameter(
            torch.FloatTensor(dim_q, dim_k).normal_() * math.sqrt(dim_k))
        self.value  = torch.nn.Parameter(
            torch.FloatTensor(dim_v, dim_k).normal_() * math.sqrt(dim_k))
 
        # Initialize the attention mask for self
        self.mask   = None
 
    def set_mask(self, m):
        self.mask = m
 
    def forward(self, x1, x2):
        # Compute the scaled dot product of the query and key, and add an attention mask
        qk = torch.matmul(x1, self.query) / math.sqrt(self.query.size(-1)) * self.mask  # Dot product + mask
        attn_weight = torch.softmax(qk, dim=-1)  # Softmax + mask
        output = torch.matmul(attn_weight, x2)  # Apply the scaled dot product to the output and the value
 
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(5, 2, 64, 64)
