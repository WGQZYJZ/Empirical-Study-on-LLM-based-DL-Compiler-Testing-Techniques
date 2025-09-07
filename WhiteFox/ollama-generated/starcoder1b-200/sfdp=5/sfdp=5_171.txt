
class Model(torch.nn.Module):
    def __init__(self, query_size=512, key_size=256):
        super().__init__()
        self.query = torch.nn.Linear(query_size, key_size)
        self.value = torch.nn.Linear(key_size, key_size)
        self.attn = torch.nn.Softmax(dim=-1)
 
    def forward(self, x1, x2):
        query  = self.query(x1)  # Compute the query from the input x1
        value  = self.value(x2)  # Compute the value from the input x2
        attn_weight = self.attn(query @ value).unsqueeze(-1) # Compute the attention weight of the scaled dot product between query and value
        output = x1 * attn_weight + x2 * (1 - attn_weight)
        return output


# Inputs to the model
x1  = torch.randn(3, 512)
x2  = torch.randn(512)
