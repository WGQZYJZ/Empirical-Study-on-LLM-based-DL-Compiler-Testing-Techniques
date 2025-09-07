
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(8, 64) 
        self.key = torch.randn(32, 64)
        self.value = torch.randn(10, 32, 64)
        self.attn_mask = (torch.triu(torch.ones([self.query.size(-2), self.key.size(-2)]).transpose(0, -1), diagonal=1) == 1).unsqueeze(0)

    def forward(self, x):
        v1 = torch.nn.functional.einsum("b n d, b m n e->b m d e", [self.query, self.key]) / math.sqrt(64.) # Compute the dot product of query and key tensors in batch mode and 32-dimensional mode
        v1 = (v1 + torch.triu(torch.ones([self.query.size(-2), self.key.size(-2)]).transpose(0, -1), diagonal=1) == 1).unsqueeze(0) @ v1 # Add the attention mask to the dot product
        v1 = torch.softmax(v1, dim=-1)
        v2 = (torch.nn.functional.einsum("b m d e, b n d e-> b m n", [v1, self.value])) 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(4096)
