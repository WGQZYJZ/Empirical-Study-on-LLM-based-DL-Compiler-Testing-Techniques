
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(8, 16) # Define a linear transformation to map the query from one dimension to another dimension 
        self.key   = torch.nn.Linear(24, 30) # Define a linear transformation to map the key from one dimension to another dimension
        self.value = torch.nn.Linear(90, 180) # Define a linear transformation to map the value from one dimension to another dimension 
        self.scale_factor = (torch.Tensor([2])**torch.arange(3)) / (3.0 * 4567.0)**(torch.Tensor([3]))  # Compute scale factor using formula 3 from Appendix A
        self.dropout_p = torch.Tensor([1e-3]) # Define a dropout probability using formula 2 from Appendix A
 
    def forward(self, qk): 
        v1  = self.query(qk) # Apply the linear transformation to the input query tensor
        v2  = self.key(v1)   # Apply the linear transformation to the output of applying the first linear transformation to the input query tensor
        v3  = torch.matmul(self.scale_factor, v2) # Compute scaled dot product using formula 1 from Appendix A 
        v4  = torch.nn.functional.softmax(v3, dim=-1) # Apply softmax to the output of computing scaled dot product
        v5  = torch.nn.functional.dropout(self.dropout_p, v4) # Apply dropout probability to the output of applying softmax 
        v6  = self.value(v5)   # Apply linear transformation using the value tensor as input
        return v6

# Initializing the model with randomly generated weights and biases
m = Model()


# Inputs to the model
qk1= torch.randn(3, 24)
__output__  = m(qk1) 

