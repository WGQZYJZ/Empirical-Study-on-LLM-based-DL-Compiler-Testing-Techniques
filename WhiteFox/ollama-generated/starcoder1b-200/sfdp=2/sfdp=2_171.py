
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 64)
        self.key   = torch.nn.Linear(128, 64)
        self.value = torch.nn.Linear(64, 1)
 
    def forward(self, x1):
        x2 = self.query(x1).unsqueeze(-2).repeat_interleave(64, dim=-2)  # Compute the output of the key as a query vector
        x3 = self.key   (x1).unsqueeze(-1).expand_as(x2)  # Compute the output of the value as a key vector
        v0  = torch.matmul(x2, x3)  # Compute the dot product of the two outputs
        v1  = v0.div(torch.sqrt(torch.FloatTensor([1e-8])))  # Scale the dot product by the sqrt(eps) constant, and then softmax to get probabilities for all elements in the resulting vector
        v2  = torch.nn.functional.dropout(v1, p=dropout_p)  # Apply dropout on the probabilities output
        v3  = self.value(x1).unsqueeze(-1)  # Use the value as a multiplier of the dot product
        v4  = v3 * v2  # Compute the sum of the two outputs
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
