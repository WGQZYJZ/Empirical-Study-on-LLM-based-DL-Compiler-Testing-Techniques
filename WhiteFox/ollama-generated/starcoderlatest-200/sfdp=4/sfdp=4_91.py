
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_proj = torch.nn.Linear(3, 8) # Apply linear projection to get query vector
        self.k_proj = torch.nn.Linear(4, 16) # Apply linear projection to get key vector
        self.v_proj = torch.nn.Linear(5, 24) # Apply linear projection to get value vector
 
    def forward(self, x):
        q = self.q_proj(x) @ 0.7071067811865476 # Use cosine similarity function in the input vector and apply a scale of 0.7071067811865476 to get query vector
        k = self.k_proj(x) @ 0.5 # Use l2 normalization on the input vector and apply a scale of 0.5 to get key vector
        v = self.v_proj(x) # Get value vector from input vector
 
        return q, k, v


# Initializing the model
m = Model()
q, k, v = m(x1)
 
