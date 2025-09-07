
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(128)) # Initialize the query parameter to random values from a normal distribution
        self.key  = torch.nn.Parameter(torch.randn(128)) # Initialize the key parameter to random values from a normal distribution
        self.value = torch.nn.Parameter(torch.randn(4096, 128)) # Initialize the value parameter to random values from a normal distribution
 
    def forward(self):
       qk  = torch.matmul(self.query, self.key) 
       scaled_qk  = qk / math.sqrt(self.query.size(-1))
       softmax_qk  = torch.nn.functional.softmax(scaled_qk)
       dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
       output  = dropout_qk.matmul(self.value)
       return output

# Initializing the model
m  = Model()

