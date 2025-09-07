
class Model(torch.nn.Module):
    def __init__(self, inv_scale=0.7978846):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot = torch.matmul(query, key.transpose(-2,-1)) / inv_scale # Apply matrix multiplication between the query and the transposed of the key vectors to get the Scaled Dot-Product Attention values
        attention_weights  = scaled_dot.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


m = Model()
 
query = torch.randn([8,32]) # A randomly generated tensor of shape [batch size, embedding dim] for the query vectors
key = torch.randn([8,32]) # A randomly generated tensor of shape [batch size, embedding dim] for the key vectors
value = torch.randn([8,64]) # A randomly generated tensor of shape [batch size, output dim] for the value vectors
 
output  = m(query,key,value)

