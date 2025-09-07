
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self,  query):
            key = torch.randn([32], requires_grad=True) # The key is an input to the model
            value = torch.randn([32], requires_grad=True) # The value is another input of the model
            qk  = torch.nn.functional.linear(query, key) + query # Compute a dot product of the query and the key
            scaled_qk  = qk.div(inv_scale_factor) 
            softmax_qk  = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
            output  = dropout_qk * value # Compute a dot product of the dropout output and a value 
            return  output

# Initializing the model
m = Model()

# Inputs to the model
query1 = torch.randn(2048)

