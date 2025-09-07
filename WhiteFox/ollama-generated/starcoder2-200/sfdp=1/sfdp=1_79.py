
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale=0.7934827536489171):  # The scale parameter is fixed here and shouldn't be replaced with a randomly generated number as it affects the result of the model.
        v = torch.matmul(query, key.transpose(-2, -1))
        scaled_v = v / scale
        softmax_v = scaled_v.softmax(dim=-1)
        dropout_v  = torch.nn.functional.dropout(softmax_v, p=0.4938657097341092) 
        output = dropout_v @ value # @ is used to denote matrix multiplication between the two tensors in this example. The @ operator can be replaced with torch.bmm()
        return output

# Initializing and inputing data for the model: 
query  = torch.randn(8, 1024)  
key  = torch.randn(8, 768) # Here we assume that query has size [N, M] where N is batch dimension (number of sequence) while M is the key length. Also in this example value contains 5639 elements and the shape of the key tensor depends on the input data so that 419832 < 768 * 5639
value = torch.randn(8, 768) # For simplicity sake we assume here that the shape of value is [N, 768] where N corresponds to number of sequence. Also in this example  value contains 5639 elements and key length depends on input data so that 419832 < 5639 * 768
m = Model() # Initialization
