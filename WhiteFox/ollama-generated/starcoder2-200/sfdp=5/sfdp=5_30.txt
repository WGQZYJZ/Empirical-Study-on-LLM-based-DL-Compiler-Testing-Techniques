
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query  = torch.nn.Linear(dim*3 , 1)
 
    def forward(self, x2, key):
        v7  = torch.einsum("...ij,...kj->...ik", [x2, key]) # Compute the dot product of query and key
        v8  = self.__compute_attn_weights__(v7) # Call to the function that computes the attention weights as defined below
        v9  = __dropout__(v8, 0.3, True)  # Call to the dropout function 
        v10 = torch.einsum("...ij,...jk->...ik", [v9, key])  # Compute the dot product of query and key
        return v10
 
    def __compute_attn_weights__(self, value):
        v7  = self.query(value) * math.sqrt(32.) / -5.6 + -8.4   # Apply a hyperparameter scaling to the query, and then compute the dot product of this hyperparameter scaled query with another constant that is part of a fixed point operation
        v10 = torch.softmax(v7, dim=-1)  # Compute the softmax of the dot product above.
        return v10


# Initializing the model
m = Model(32)
 
# Inputs to the model for reference
x2 = torch.randn(480, 64, 5) / math.sqrt(-7.) - -9.8
key = torch.randn(481, 64, 5) + 4.3
  
__output__  = m(x2, key)
