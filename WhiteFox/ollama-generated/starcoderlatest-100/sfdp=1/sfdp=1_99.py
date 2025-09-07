
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_per_head=128):
        super().__init__()
 
        self.q = torch.nn.Linear(3, 10)
        self.k = torch.nn.Linear(4, 10)
        self.v = torch.nn.Linear(5, 10)

        self.num_heads = 2
 
    def forward(self, x):
        query, key, value = self.q(x).split(3, dim=-1) # Split tensor to three tensors along dimension -1
        key, value = torch.split(key, dim=-1, chunks=self.num_heads) # Split tensor to two tensors of 2 parts along dimension -1

        output = []
        for i in range(self.num_heads):
            head_qk = torch.matmul(query, key[i].transpose(-2, -1)) # Compute the dot product of the query and key tensors
            scaled_head_qk = head_qk.div(math.sqrt(float(self.dim_per_head))) # Scale the dot product by sqrt(float(self.dim_per_head))
            softmax_head_qk = scaled_head_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
            dropout_head_qk = torch.nn.functional.dropout(softmax_head_qk, p=dropout_p) # Apply dropout to the softmax output

            head_v = torch.matmul(dropout_head_qk, value[i]) # Compute the dot product of the dropout output and the value tensor
            output.append(head_v)

        return torch.cat(output, dim=-1)
# Initializing the model
m = MultiHeadAttention()

# Inputs to the model
x = torch.randn(32, 64, 64)
