
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 64, 64))
        self.key   = torch.nn.Parameter(torch.randn(1, 64, 64))
        self.value = torch.nn.Parameter(torch.randn(1, 8, 56, 56))
        self.attn_mask = torch.zeros(1, 1, 1024, dtype=torch.bool)
        self.attn_mask.fill_(True) # Fill the attention mask to make the key dimensionality unmatched to value's dimensionality
        self.weight = torch.nn.Parameter(torch.randn(1, 8, 56, 56))
 
    def forward(self, x):
        qk   = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))
        q    = F.softmax(qk, dim=-1) @ self.value # compute weighted sum of value and attention weights
        output = torch.einsum('bkc,bmd->bcd', [q, x]) # compute the dot product of weight and value
        return output
 

# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(1, 64, 64)
# Outputs from the model
