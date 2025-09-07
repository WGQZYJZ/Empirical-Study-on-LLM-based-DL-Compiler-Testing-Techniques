
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_query = torch.nn.Linear(20, 8) # Project each query in the queries matrix into a fixed-length vector representation using linear layers
        self.linear_value = torch.nn.Linear(20, 4) # Project each value in the keys matrix into a fixed-length vector representation using linear layers
 
        self.linear_key = torch.nn.Linear(20, 8)
        self.linear_attn = torch.nn.Linear(8, 1)
 
    def forward(self, queries, values):
        qk = torch.matmul(queries, self.linear_query.weight).transpose(-1, -2) / math.sqrt(queries.size(-1))
        # Scale the dot product by dividing it with square root of the number of query dimensions
        attn_mask  = (queries * 0.5 + queries[:, None] * 0.5) * 2 # Set all negative values to -0.5, and set all positive values to +0.5
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax on the result of adding a constant scalar to each query in queries
        output = torch.matmul(attn_weight, self.linear_value.weight) # Compute weighted sum of values
        return output
 

# Initializing the model
m = Model()

# Inputs to the model
queries = torch.randn(100, 20)
values = torch.randn(200, 20)
