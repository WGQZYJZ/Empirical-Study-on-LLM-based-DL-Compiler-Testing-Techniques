
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(32, 64)
        self.attention_weights = None
 
    def forward(self, query, key, value):
        scaled_dot_product = self.scaled_dot_product(query @ key.transpose(-2, -1)) / sqrt(key.size(-1))
        self.attention_weights  = scaled_dot_product.softmax(dim=-1)

        return self.attention_weights.matmul(value)

# Initializing the model and inputs to the model
m = Model()
inv_scale = torch.tensor([0.98765]) # scaling factor is not used in practice, but in the example here for illustration purposes only
query  = torch.randn(2,32) 
key   = torch.randn(4,1,32).transpose(-2,-1) + inv_scale 
value = key + torch.tensor([0.5]) # some more tensors to be used in practice; in the example here for illustration purposes only
__output__  = m(query, key, value)

