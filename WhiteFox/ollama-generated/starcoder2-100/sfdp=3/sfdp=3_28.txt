
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
         v1 = torch.matmul(query1, key2.transpose(-2, -1))  # Compute the dot product of a query and a key tensor 
         v4 = torch.nn.functional.softmax(v1)
         v5 = dropout_qk(v4)
         v6 = v3 * v5
        return v6
 
# Initializing model
m  = Model()

 # Inputs to the model 
query2  = torch.randn(3, 7, 9, 10)  # Initialize query tensor with shape (3, 7, 9, 10).
key4  = torch.randn(5, 6, 8, 10)  # Initialize key tensor with shape (5, 6, 8, 10).
value2 = torch.randn(4, 7, 8, 10)  # Initialize value tensor with shape (4, 7, 8, 10).

# Output of the model on given input tensors 
__output__  = m(query2, key4, value3)

