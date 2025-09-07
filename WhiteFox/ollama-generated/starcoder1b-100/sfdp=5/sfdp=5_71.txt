
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key   = torch.nn.Linear(3, 5)
        self.value = torch.nn.Linear(3, 6)

    def forward(self, x1, x2):
        query_t1 = self.query(x1) # Apply linear layer to the input x1
        key_t2   = self.key(x2)  # Apply linear layer to the input x2
        t3       = torch.mul(query_t1, key_t2) / math.sqrt(query_t1.size(-1)) # Compute dot product of query and key, scale it with sqrt(m_1 * m_2), store the result into variable v
        t4       = torch.exp(-t3)  # Apply exponentiation function to the value of the dot product (result will be a Tensor of shape (n1, n2))
        t5       = t4 + 1    # Add a constant to the result, store the result into variable v
        t6       = torch.mul(t5, self.value(x1)) # Multiply the result of the dot product by value from input x1
        return t6


# Initializing the model
m  = Model()


