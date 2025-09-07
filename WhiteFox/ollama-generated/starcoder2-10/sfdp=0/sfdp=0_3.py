
class AttentionBlock(torch.nn.Module):
    def __init__(self, query_dimension=2048, value_dimension=512, num_heads=36):
        super().__init__()
 
        self.query_dimension = query_dimension
        self.value_dimension = value_dimension
 
        self.num_heads  = min(num_heads, query_dimension//self.query_dimension)
 
        self.linear_query  = torch.nn.Linear(query_dimension, self.num_heads * self.query_dimension)
        self.linear_key  = torch.nn.Linear(value_dimension, self.num_heads * value_dimension)
 
        self.scale  = float(self.query_dimension)**-0.5
 
    def forward(self, query):
        v1  = self.linear_query(query).reshape(-1, self.num_heads, self.query_dimension)
        v2  = self.linear_key(query).reshape(-1, self.num_heads, value_dimension//self.num_heads)
 
        v3  = torch.matmul(v1/float(self.scale), v2.transpose(-2,-1)) / float(self.num_heads)**0.5
        v4  = v3.softmax(dim=-1)

        output  = v4.matmul(v2).reshape(*query.shape)
        return output


# Initializing the model with some dummy parameters to get the shapes right for the tensors in the forward method. You can then replace these values when actually initializing your model.
b  = AttentionBlock()

# Inputs to the model. These are not correct and are used as an example. Feel free to use different shapes or number of elements in this array.
x1  = torch.randn(3,50)

 # You can replace these dummy values with actual input parameters.
# 