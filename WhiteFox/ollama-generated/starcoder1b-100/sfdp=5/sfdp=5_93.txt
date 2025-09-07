
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 512)
        self.ffn = torch.nn.Linear(512, 384)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.attn.weight) / math.sqrt(torch.size(x1)[-1]) # Compute the dot product of the query and key
        qk = torch.nn.functional.softmax(qk, dim=-1)  # Apply softmax to the result
        output = torch.matmul(qk, self.value.weight) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m  = Model()


