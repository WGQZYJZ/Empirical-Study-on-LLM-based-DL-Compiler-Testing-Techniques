
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 3) # Create a fully connected layer to project the query from dimension 10 to dimension 3
        self.key = torch.nn.Linear(5, 4) # Create a fully connected layer to project the key from dimension 5 to dimension 4
        self.value = torch.nn.Linear(7, 6) # Create a fully connected layer to project the value from dimension 7 to dimension 6
 
    def forward(self, x):
        v1  = self.query(x) # Project query using a linear layer of input size 3 to output size 5
        v2  = self.key(v1) # Project key using another fully connected layer with input size 4 and output size 7 
        v3  = torch.nn.functional.dropout(torch.nn.functional.softmax(
            torch.matmul(
                torch.div(
                    torch.matmul(
                        v2, 
                        v2.transpose(-2, -1) # Compute the dot product of the projected key and its transpose 
                    ), inv_scale_factor), 0
        )), p=dropout_p)) # Apply dropout with probability of 5%
        v4 = v3.matmul(self.value(v1)) # Compute the dot product of the dropout output and value after projecting it to another fully connected layer 
        return v4


# Initializing the model:
m = Model() 

# Inputs to the model (assume that the input size is 5):
query_input  = torch.randn(3, 10) # A tensor with shape [3 x 10]
key_input  = torch.randn(7, 4) # A tensor with shape [7 x 4] 

__output__   = m(query_input) # The output of the model after applying dropout and dot product operations

