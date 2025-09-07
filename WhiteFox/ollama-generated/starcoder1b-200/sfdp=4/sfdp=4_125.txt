
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 256)
        self.linear2 = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        qk = (x1 @ x1).softmax(-1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        value = self.linear1(x1)  # Compute the dot product of the attention weights and the value
        output = attn_weight @ value  # Compute the weighted sum of the value tensor
        return output


# Initializing the model
m = Model()

