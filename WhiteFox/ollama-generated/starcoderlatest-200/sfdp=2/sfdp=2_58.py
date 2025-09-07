
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 512)
 
    def forward(self, x1):
        h1 = self.linear(x1) # Linear operation between query and key for computing the dot product of queries with keys
        scaled_h1 = h1 / 128 # Scale the output of linear layer to a fixed constant
        softmax_scaled_h1 = scaled_h1.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_scaled_h1 = torch.nn.functional.dropout(softmax_scaled_h1, p=0.5) # Apply dropout to the softmax output
        h2 = dropout_scaled_h1 @ self.linear.weight # Compute the dot product of the dropout output and the weights of linear layer
        return h2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 256, 64)
