
class Model(torch.nn.Module):
    def __init__(self,
                 dim_query: int, 
                 dim_key: int, 
                 dim_value: int,
                 num_heads: int,
                 dropout_p: float):
        super().__init__()
        
        # Set the number of input and output channels to 32
        self.dim_query = dim_query 
        self.dim_key = dim_key 
        self.dim_value = dim_value
        self.num_heads = num_heads
        self.dropout_p = dropout_p
 
        # Initialize the embedding layer for the query, key and value tensor
        self.embedding  = torch.nn.Embedding(1000, self.dim_query)
 
    def forward(self, x):
        # Generate three input tensors with different shapes for the query, key, and value tensor
        q = self.embedding(x[:, 0].unsqueeze(-1)).squeeze(-1)
        k = self.embedding(x[:, 1].unsqueeze(-1)).squeeze(-1)
        v = self.embedding(x[:, 2].unsqueeze(-1)).squeeze(-1)
 
        # Calculate the dot product of the query, key and value tensor using a customized attention function
        output = attention(q, k, v)
 
        return output


# Input tensor for the model
input_tensor = torch.randint(0, high=1000, size=(3, 2)) 
