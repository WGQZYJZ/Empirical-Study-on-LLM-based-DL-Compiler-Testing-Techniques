
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.query * self.key # Compute the dot product of query and key tensors.
        v3 = torch.nn.functional.normalize(v2) / torch.sqrt(torch.tensor([768], dtype=x1.dtype)) # Normalize by the square root of the number of features.
        v4  = self.softmax(v3) # Compute softmax over the dot product.
        v5 = torch.nn.functional.dropout(v4, p=self.dropout_p) * self.value  # Compute the dropout with a probability of 0.1 and a value.
        return v5
# Initializing the model
m = Model()
 
# Inputs to the model.
x1  = torch.randn(23, 768)
x2  = torch.randn(23, 768)
__output__   = m(x1, x2)

