
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, query):
        k1 = query @ key # Compute the dot product of the query and the key
        k2 = query.matmul(key.transpose(-2, -1))  # Compute the dot product of the query and the key
        v1  = self.linear(query)   # Apply linear layer to the query 
        scaled_k1 = torch.nn.functional.dropout(k1.div(0.5), p=0.34862792956878845) # Divide dot product by 0.5
        scaled_k2 = k2 / 0.5   # Divide the dot product of the query and key by 0.5 
        return v1, scaled_k1, scaled_k2


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3)
key = torch.randn(5, 3)

__output__, __scaled-qk1__, __scaled-qk2__  = m(query)


